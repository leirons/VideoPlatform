from fastapi.testclient import TestClient

import unittest

from core.db import SessionLocal

from services.user.logic import UserLogic
from asyncio import run

from app.api import app

client = TestClient(app)

openapi_schema = {"openapi": "3.0.2", "info": {"title": "FastAPI", "version": "0.1.0"}, "paths": {"/user/": {
    "post": {"tags": ["User"], "summary": "Create User", "operationId": "create_user_user__post",
             "requestBody": {"content": {"application/json": {"schema": {"$ref": "#/components/schemas/UserCreate"}}},
                             "required": True}, "responses": {"200": {"description": "Successful Response", "content": {
            "application/json": {"schema": {"$ref": "#/components/schemas/User"}}}},
                                                              "422": {"description": "Validation Error", "content": {
                                                                  "application/json": {"schema": {
                                                                      "$ref": "#/components/schemas/HTTPValidationError"}}}}}}},
    "/user/{user_id}": {
        "get": {"tags": [
            "User"],
            "summary": "Get User",
            "operationId": "get_user_user__user_id__get",
            "parameters": [
                {
                    "required": True,
                    "schema": {
                        "title": "Id of user",
                        "type": "integer"},
                    "name": "user_id",
                    "in": "path"}],
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/User"}}}},
                "422": {
                    "description": "Validation Error",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/HTTPValidationError"}}}}}},
        "put": {"tags": [
            "User"],
            "summary": "Put User",
            "operationId": "put_user_user__user_id__put",
            "parameters": [
                {
                    "required": True,
                    "schema": {
                        "title": "User Id",
                        "type": "integer"},
                    "name": "user_id",
                    "in": "path"}],
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserCreate"}}},
                "required": True},
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "schema": {}}}},
                "422": {
                    "description": "Validation Error",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/HTTPValidationError"}}}}}},
        "delete": {
            "tags": [
                "User"],
            "summary": "Get User",
            "operationId": "get_user_user__user_id__delete",
            "parameters": [
                {
                    "required": True,
                    "schema": {
                        "title": "Id of user",
                        "type": "integer"},
                    "name": "user_id",
                    "in": "path"}],
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "schema": {}}}},
                "422": {
                    "description": "Validation Error",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/HTTPValidationError"}}}}}},
        "patch": {
            "tags": [
                "User"],
            "summary": "Patch User",
            "operationId": "patch_user_user__user_id__patch",
            "parameters": [
                {
                    "required": True,
                    "schema": {
                        "title": "User Id",
                        "type": "integer"},
                    "name": "user_id",
                    "in": "path"}],
            "requestBody": {
                "content": {
                    "application/json": {
                        "schema": {
                            "$ref": "#/components/schemas/UserPatch"}}},
                "required": True},
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "schema": {}}}},
                "422": {
                    "description": "Validation Error",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/HTTPValidationError"}}}}}}},
    "/user-list/": {
        "get": {"tags": [
            "User"],
            "summary": "Get All User",
            "operationId": "get_all_user_user_list__get",
            "parameters": [
                {
                    "required": False,
                    "schema": {
                        "title": "Skip",
                        "type": "integer",
                        "default": 0},
                    "name": "skip",
                    "in": "query"},
                {
                    "required": False,
                    "schema": {
                        "title": "Limit",
                        "type": "integer",
                        "default": 100},
                    "name": "limit",
                    "in": "query"}],
            "responses": {
                "200": {
                    "description": "Successful Response",
                    "content": {
                        "application/json": {
                            "schema": {
                                "title": "Response Get All User User List  Get",
                                "type": "array",
                                "items": {
                                    "$ref": "#/components/schemas/User"}}}}},
                "422": {
                    "description": "Validation Error",
                    "content": {
                        "application/json": {
                            "schema": {
                                "$ref": "#/components/schemas/HTTPValidationError"}}}}}}}},
                  "components": {"schemas": {"HTTPValidationError": {"title": "HTTPValidationError", "type": "object",
                                                                     "properties": {
                                                                         "detail": {"title": "Detail", "type": "array",
                                                                                    "items": {
                                                                                        "$ref": "#/components/schemas/ValidationError"}}}},
                                             "User": {"title": "User",
                                                      "required": ["email", "id", "login", "hash_password"],
                                                      "type": "object",
                                                      "properties": {"email": {"title": "Email", "type": "string"},
                                                                     "id": {"title": "Id", "type": "integer"},
                                                                     "login": {"title": "Login", "type": "string"},
                                                                     "hash_password": {"title": "Hash Password",
                                                                                       "type": "string"}}},
                                             "UserCreate": {"title": "UserCreate",
                                                            "required": ["email", "password", "login"],
                                                            "type": "object", "properties": {
                                                     "email": {"title": "Email", "type": "string"},
                                                     "password": {"title": "Password", "type": "string"},
                                                     "login": {"title": "Login", "type": "string"}}},
                                             "UserPatch": {"title": "UserPatch", "type": "object",
                                                           "properties": {"login": {"title": "Login", "type": "string"},
                                                                          "email": {"title": "Email", "type": "string"},
                                                                          "password": {"title": "Password",
                                                                                       "type": "string"}}},
                                             "ValidationError": {"title": "ValidationError",
                                                                 "required": ["loc", "msg", "type"], "type": "object",
                                                                 "properties": {
                                                                     "loc": {"title": "Location", "type": "array",
                                                                             "items": {"type": "string"}},
                                                                     "msg": {"title": "Message", "type": "string"},
                                                                     "type": {"title": "Error Type",
                                                                              "type": "string"}}}}}}


class LogicTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.db = SessionLocal()
        self.logic = UserLogic()

    def test_openapi(self):
        response = client.get("/openapi.json")
        assert response.status_code == 200, response.text
        assert response.json() == openapi_schema

    def test_create(self):
        data = {
            "email": "test1@gmail.com",
            "login": "string",
            "password": "password"
        }
        response = client.post("/user/", json=data)
        assert response.status_code == 200

    def test_delete(self):
        user = run(self.logic.get_user_by_email(self.db, "test1@gmail.com"))
        response = client.delete(f"/user/{user.id}")
        assert response.status_code == 200


if __name__ == '__main__':
    unittest.main()
