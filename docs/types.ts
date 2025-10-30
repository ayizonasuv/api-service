interface ApiResponse<T> {
  data: T;
  status: number;
  statusText: string;
  headers: Record<string, string>;
}

interface ApiError {
  message: string;
  code: number;
  details?: Record<string, unknown>;
}

interface PaginatedResponse<T> {
  items: T[];
  total: number;
  page: number;
  pageSize: number;
}

interface User {
  id: string;
  name: string;
  email: string;
  createdAt: string;
  updatedAt: string;
}

interface CreateUserPayload {
  name: string;
  email: string;
  password: string;
}

interface UpdateUserPayload {
  name?: string;
  email?: string;
  password?: string;
}

export type {
  ApiResponse,
  ApiError,
  PaginatedResponse,
  User,
  CreateUserPayload,
  UpdateUserPayload,
};