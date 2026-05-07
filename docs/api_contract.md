---
#API contract user login
**Endpoint":** /api/v1/login
**Method":** POST
**Request Body (JSON):**
{
"email": "nazwa@univ.ac.id",
"pw": "abc123"
}
**Response Body (JSON):**
{
"status": "success",
"token": "abc123",
"message": "Login berhasil"
}
