# Flake used for development with nix
{
  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-24.05";
    flake-utils.url = "github:numtide/flake-utils";
  };

  outputs = inputs:
    inputs.flake-utils.lib.eachDefaultSystem (system:
      let
        pkgs = import inputs.nixpkgs { inherit system; };
      in
      {
        devShell = pkgs.mkShell {
          packages = with pkgs; [
            # = blog =
            doxygen
            (python3.withPackages (ps: [
              ps.pelican
              ps.pygments
              ps.pillow
              ps.livereload
              ps.invoke
            ]))
            (pkgs.texlive.combine {
              inherit (pkgs.texlive)
                scheme-basic
                ucs
                gensymb
                newtx
                etoolbox
                xstring
                xcolor
                fontaxes
                preview
                tex-gyre
                dvisvgm
                xpatch
                standalone;
            })
          ];
        };
      });
}
