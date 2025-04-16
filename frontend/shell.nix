{ pkgs ? import <nixpkgs> {} }:

pkgs.mkShell {
  name = "nuxt-frontend-dev";

  buildInputs = [
    pkgs.nodejs_18
    pkgs.nodePackages.pnpm
  ];

  shellHook = ''
    echo "✅ Nuxt + pnpm Umgebung aktiviert"
  '';
}
