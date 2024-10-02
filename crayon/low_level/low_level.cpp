#include <cpr/cpr.h>

#include <iostream>
#include <string>

class Ville {
 private:
  std::string nom;
  int code_postal;
  int prixm2;

 public:
  // Constructeur
  Ville(const std::string& nom, int code_postal, int prixm2)
      : nom(nom), code_postal(code_postal), prixm2(prixm2) {}

  // méthode d'affichage
  void afficher() const {
    std::cout << "Nom de la ville: " << nom << std::endl;
    std::cout << "Code postal: " << code_postal << std::endl;
    std::cout << "Prix au m²: " << prixm2 << "€" << std::endl;
  }
};

// Fonction principale
int main(int argc, char** argv) {
  // instance de Ville
  Ville ville("toulouse", 31200, 5000);

  // Affichage de la ville
  ville.afficher();

  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/Ville/1"});
  //  cpr::Authentication{"AmiraLABDOUNI", "Futurcareer123_",
  //  cpr::AuthMode::BASIC},
  //    cpr::Parameters{{"anon", "true"}, {"key", "value"}});
  // r.status_code;                  // 200
  // r.header["content-type"];       // application/json; charset=utf-8
  // r.text;                         // JSON text string

  if (r.status_code == 200) {  // pour verifier si c vrai
    std::cout << "La réponse est : " << r.text << std::endl;
  } else {
    std::cout << "Erreur lors de la requête : " << r.status_code << std::endl;
  }
  return 0;
}
