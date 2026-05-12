





import java.util.List;
import java.util.ArrayList;

public class __table___T_CompteDeLUtilisateur  {

    private String type;
    private String pseudo;
    private int numeroUtilisateur;
    private String motDePasse;
    private String adresseMail;



    public __table___T_CompteDeLUtilisateur(
        String type,        String pseudo,        int numeroUtilisateur,        String motDePasse,        String adresseMail    ) {
        this.type = type;
        this.pseudo = pseudo;
        this.numeroUtilisateur = numeroUtilisateur;
        this.motDePasse = motDePasse;
        this.adresseMail = adresseMail;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getPseudo() {
        return pseudo;
    }

    public void setPseudo(String pseudo) {
        this.pseudo = pseudo;
    }
    public int getNumeroutilisateur() {
        return numeroUtilisateur;
    }

    public void setNumeroutilisateur(int numeroUtilisateur) {
        this.numeroUtilisateur = numeroUtilisateur;
    }
    public String getMotdepasse() {
        return motDePasse;
    }

    public void setMotdepasse(String motDePasse) {
        this.motDePasse = motDePasse;
    }
    public String getAdressemail() {
        return adresseMail;
    }

    public void setAdressemail(String adresseMail) {
        this.adresseMail = adresseMail;
    }


}