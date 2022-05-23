with import <nixpkgs> {};

stdenv.mkDerivation {
  pname = "vimwiki-diary-template";
  version = "0.0";

  src = ./.;

  buildInputs = [ python3 ];

  installPhase = ''
    install -D vimwiki-diary-template.py $out/vimwiki-diary-template
  '';

  meta = with lib; {
    description = "vimwiki-diary-template";
    homepage = "https://github.com/jboynyc/vimwiki-diary-template";
    license = licenses.agpl3Plus;
  };
}
