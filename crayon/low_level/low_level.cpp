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

  // Constructeur avec l'ID, récupère les données via une requête HTTP
  Ville(int id) : id(id) {
    std::string url = "http://localhost:8000/Ville/" + std::to_string(id);
    cpr::Response r = cpr::Get(cpr::Url{url});
    if (r.status_code == 200) {
      nlohmann::json json_response = nlohmann::json::parse(r.text);
      nom = json_response["nom"];
      code_postal = json_response["code_postal"];
      prixm2 = json_response["prixm2"];
      this->id = id;
    } else {
      std::cerr << "Erreur de récupération des données pour l'ID: " << id
                << std::endl;
    }
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

/*class QuantiteRessource {

 private:

  Ressource* ressource;
  int quantite;
  int id;

 public:
  // Constructeur
  QuantiteRessource( const std::  Ressource* ressource, int quantite, int id ) :
ressource(ressource), quantite(quantite),id(id) {}

  QuantiteRessource(const nlohmann::json& json_data) {
    ressource= json_data["ressource"];
    quantite = json_data["quantite"];
    id = json_data["ID"];
  }

  // méthode d'affichage
  void afficher() const {
    std::cout << "ressource: " << ressource<< std::endl;//quantite *
ressource->prix std::cout << "quantite: " << quantite<< std::endl; std::cout <<
",ID : " <<id << std::endl;
  }

};*/

/*class Etape {

private:
    std::string nom;
    Machine* machine;
    QuantiteRessource* quantiteRessource;
    int duree;
    Etape* etapeSuivante;
    int id;

public:
    // Constructeur
    Etape( const std::string nom, Machine* machine, QuantiteRessource*
quantiteRessource, int duree, Etape* etapeSuivante = nullptr,int id) : nom(nom),
machine(machine), quantiteRessource(quantiteRessource), duree(duree),
etapeSuivante(etapeSuivante),int (id) {}

    Etape(const nlohmann::json& json_data) {
          nom = json_data["nom"];
          machine= json_data["machine"];
          quantiteRessource = json_data["QuantiteRessource"];
          duree= json_data["duree"];
          etapeSuivante = json_data["etapeSuivante"];
          id = json_data["ID"];
        }

    void afficher() const {
          std::cout << "Nom : " << nom << std::endl;
          std::cout << "Machine: " <<machine << std::endl;
          std::cout << "quantite Ressource: " << quantiteRessource << std::endl;
          std::cout << "durée : " <<duree << std::endl;
          std::cout << "etape suivante: " <<etapeSuivante << std::endl;
          std::cout << ",ID : " <<id << std::endl;
        }

};*/

/*class Objet {

private:

  std::string nom;
  int prix;
  int id;

public:
    // Constructeur
    Objet( const std::string nom, int prix, int id ) : nom(nom) , prix(prix),int
(id)  {}

    Objet(const nlohmann::json& json_data) {
        nom = json_data["nom"];
        prix= json_data["prix"];
        id = json_data["ID"];
      }

  void afficher() const {
        std::cout << "Nom : " << nom << std::endl;
        std::cout << "Prix " << prix << "€" << std::endl;
        std::cout << ",ID : " <<id << std::endl;
      }


};*/

/*class Produit : public Objet {

private:

  Etape* premiereEtape;
  int id;
public:
    // Constructeur
  Produit( const std::string nom, int prix, Etape* premiereEtape) : Objet(nom,
prix), premiereEtape(premiereEtape),int (id)  {}

  Produit(const nlohmann::json& json_data) {
        nom = json_data["objet.nom"];
        prix= json_data["objet.prix"];
        premiereEtape = json_data["premiereEtape"];
        id = json_data["ID"];
      }

  void afficher() const {
        std::cout << "Nom : " << objet.nom << std::endl;
        std::cout << "Prix: " <<objet.prix<< std::endl;
        std::cout << "Première étape : " <<  premiereEtape << std::endl;
        std::cout << ",ID : " <<id << std::endl;
      }
  };*/

// Fonction principale
int main(int argc, char** argv) {
  // instance de Ville
  // Ville ville23("toulouse", 31200, 5000, 3);

  // Affichage de la ville
  // Ville.afficher();

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
    int ID_ville = json_response["ID"];

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
  // a l'aide du constructeur id
  int id = 1;
  Ville ville(id);
  ville.afficher();
  return 0;
}

/*class Ressource : public Objet {
public:
    Ressource(std::string nom, int prix) : Objet(nom, prix) {}


};*/
/*class Machine {
public:
    std::string nom;
    int prix;
    int n_serie;

    Machine(std::string nom, int prix, int n_serie) : nom(nom), prix(prix),
n_serie(n_serie) {}


};*/

/*class Local {
public:
    std::string nom;
    Ville* ville;
    int surface;

    Local(std::string nom, Ville* ville, int surface) : nom(nom), ville(ville),
surface(surface) {}


};*/
/*class Usine : public Local {
public:
    std::vector<Machine> machines;

    Usine(std::string nom, Ville* ville, int surface) : Local(nom, ville,
surface) {}

    void addMachine(const Machine& machine) {
        machines.push_back(machine);
    }


    int costs() const {
        int totalCost = 0;
        for (const auto& machine : machines) {
            totalCost += machine.costs();
        }
        return totalCost + (surface * ville->prixm2);
    }
};*/
/*class Stock {
public:
    Ressource* ressource;
    int nombre;
    Usine* usine;

    Stock(Ressource* ressource, int nombre, Usine* usine) :
ressource(ressource), nombre(nombre), usine(usine) {}


};*/
