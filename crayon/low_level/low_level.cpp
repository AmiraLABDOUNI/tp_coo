#include <cpr/cpr.h>

#include <iostream>
#include <nlohmann/json.hpp>
#include <string>

class Ville {
 private:
  std::string nom;
  int code_postal;
  int prixm2;
  int id;

 public:
  // Constructeur
  Ville(const std::string& nom, int code_postal, int prixm2, int id)
      : nom(nom), code_postal(code_postal), prixm2(prixm2), id(id) {}

  Ville(const nlohmann::json& json_data) {
    nom = json_data["nom"];
    code_postal = json_data["code_postal"];
    prixm2 = json_data["prixm2"];
    id = json_data["ID"];
  }

  // méthode d'affichage
  void afficher() const {
    std::cout << "Nom de la ville: " << nom << std::endl;
    std::cout << "Code postal: " << code_postal << std::endl;
    std::cout << "Prix au m²: " << prixm2 << "€" << std::endl;
  }
  void afficherr() const {
    std::cout << "Villeee: " << nom << ", Code Postal: " << code_postal
              << ", Prix au m²: " << prixm2 << ", ID: " << id << std::endl;
  }
};

// Fonction principale
int main(int argc, char** argv) {
  // instance de Ville
  Ville ville("toulouse", 31200, 5000, 3);

  // Affichage de la ville
  ville.afficher();

  cpr::Response r = cpr::Get(cpr::Url{"http://localhost:8000/Ville/1"});
  //  cpr::Authentication{"AmiraLABDOUNI", "Futurcareer123_",
  //  cpr::AuthMode::BASIC},
  //    cpr::Parameters{{"anon", "true"}, {"key", "value"}});
  // r.status_code;                  // 200
  // r.header["content-type"];       // application/json; charset=utf-8
  // r.text;                         // JSON text string

  if (r.status_code == 200) {  // Vérifier si la requête est réussie
    std::cout << "La réponse est : " << r.text << std::endl;

    // Parsing du JSON
    // try {
    auto json_response = nlohmann::json::parse(r.text);

    // Supposons que le JSON ait les clés "nom", "code_postal", et "prixm2"
    std::string nom_ville = json_response["nom"];
    int code_postal_ville = json_response["code_postal"];
    int prixm2_ville = json_response["prixm2"];
    int ID_ville = json_response["id"];

    // Créer une nouvelle instance de Ville avec les données récupérées
    Ville nouvelle_ville(nom_ville, code_postal_ville, prixm2_ville, ID_ville);

    // Afficher les informations de la nouvelle ville
    nouvelle_ville.afficher();
    Ville nouvelleville(json_response);
    nouvelleville.afficherr();
    //  }

  } else {
    std::cout << "Erreur lors de la requête : " << r.status_code << std::endl;
  }

  return 0;
}
