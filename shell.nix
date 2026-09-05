{ pkgs ? import <nixpkgs> { } }:

pkgs.mkShell {
  buildInputs = [
    (pkgs.python3.withPackages (ps: with ps; [
      torch
      torchvision
      transformers
      shap
      numpy
      pillow
      scikit-learn
      matplotlib
      opencv4
      pandas
      ipykernel
      nbformat
      nbconvert
      jupyter-client
    ]))
    (pkgs.texlive.combine {
      inherit (pkgs.texlive)
        scheme-medium latexmk booktabs caption float hyperref
        graphics xcolor geometry babel-spanish hyphen-spanish
        biblatex biber csquotes microtype;
    })
    pkgs.git
    pkgs.zip
  ];

  shellHook = ''
    export PYTHONNOUSERSITE=1
    export TOKENIZERS_PARALLELISM=false
    export OMP_NUM_THREADS=16
  '';
}
