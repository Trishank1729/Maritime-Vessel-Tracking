from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from .serializers import (
    CustomTokenObtainPairSerializer,
    UserRegistrationSerializer,
    UserSerializer,
    UserDetailSerializer,
)

User = get_user_model()


@api_view(['GET'])
@permission_classes([AllowAny])
def api_root(request):
    """
    API Root - Shows all available endpoints
    """
    return Response({
        'message': 'Maritime Vessel Tracking API',
        'version': '1.0.0',
        'endpoints': {
            'auth': {
                'login': 'POST /api/login/ - Obtain JWT tokens',
                'register': 'POST /api/register/ - Register a new user',
                'token_refresh': 'POST /api/token/refresh/ - Refresh JWT token',
            },
            'profile': {
                'get_profile': 'GET /api/profile/ - Get your profile',
                'update_profile': 'PUT /api/profile/update/ - Update your profile',
            },
            'users': {
                'list_users': 'GET /api/users/ - List all users (admin only)',
                'get_user': 'GET /api/users/<id>/ - Get specific user',
                'update_user': 'PUT /api/users/<id>/ - Update specific user',
            },
            'stats': {
                'user_stats': 'GET /api/stats/ - Get user statistics (admin only)',
            }
        },
        'documentation': 'See endpoints above for usage instructions'
    })


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    """
    Register a new user
    Expected fields: username, email, password, password_confirm, fullname
    """
    if request.method == 'POST':
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(
                {
                    'detail': 'User registered successfully',
                    'user': UserSerializer(user).data
                },
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    """
    Get authenticated user's profile
    """
    user = request.user
    serializer = UserDetailSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_profile(request):
    """
    Update authenticated user's profile
    Can update: fullname, email
    """
    user = request.user
    
    if 'fullname' in request.data:
        user.fullname = request.data['fullname']
    if 'email' in request.data:
        user.email = request.data['email']
    
    user.save()
    serializer = UserDetailSerializer(user)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    """
    Get all users (only accessible to admin)
    """
    if not request.user.is_staff:
        return Response(
            {'detail': 'Permission denied'},
            status=status.HTTP_403_FORBIDDEN
        )
    
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def user_detail(request, pk):
    """
    Get or update a specific user
    """
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response(
            {'detail': 'User not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    
    if request.method == 'GET':
        serializer = UserDetailSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        # Only allow users to update their own profile or admin update others
        if request.user.id != user.id and not request.user.is_staff:
            return Response(
                {'detail': 'Permission denied'},
                status=status.HTTP_403_FORBIDDEN
            )
        
        serializer = UserDetailSerializer(user, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_user_stats(request):
    """
    Get general user statistics (for admin/dashboard)
    """
    if not request.user.is_staff:
        return Response(
            {'detail': 'Permission denied'},
            status=status.HTTP_403_FORBIDDEN
        )
    
    stats = {
        'total_users': User.objects.count(),
        'operators': User.objects.filter(role='operator').count(),
        'analysts': User.objects.filter(role='analyst').count(),
        'admins': User.objects.filter(role='admin').count(),
    }
    return Response(stats, status=status.HTTP_200_OK)
