





import java.util.List;
import java.util.ArrayList;

public class Client  {

    private String contact;
    private String ville;
    private String nom;
    private String codePostal;
    private String tel;
    private String adresse;



    public Client(
        String contact,        String ville,        String nom,        String codePostal,        String tel,        String adresse    ) {
        this.contact = contact;
        this.ville = ville;
        this.nom = nom;
        this.codePostal = codePostal;
        this.tel = tel;
        this.adresse = adresse;
    }


    public String getContact() {
        return contact;
    }

    public void setContact(String contact) {
        this.contact = contact;
    }
    public String getVille() {
        return ville;
    }

    public void setVille(String ville) {
        this.ville = ville;
    }
    public String getNom() {
        return nom;
    }

    public void setNom(String nom) {
        this.nom = nom;
    }
    public String getCodepostal() {
        return codePostal;
    }

    public void setCodepostal(String codePostal) {
        this.codePostal = codePostal;
    }
    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }
    public String getAdresse() {
        return adresse;
    }

    public void setAdresse(String adresse) {
        this.adresse = adresse;
    }


}