{ pkgs ? import <nixpkgs> {} }:

let
  pythonEnv = pkgs.python311.withPackages (ps: with ps; [
    pip
    fastapi
    uvicorn
    psycopg2
    requests
    pytest
    sqlalchemy
    python-dotenv
    jinja2
    pyyaml
  ]);
in

pkgs.mkShell {
  name = "fastapi-backend-dev";

  buildInputs = [
    pythonEnv
  ];

  shellHook = ''
    echo "✅ Python FastAPI Devshell active"
    export PYTHONPATH=$PWD
  '';
}
