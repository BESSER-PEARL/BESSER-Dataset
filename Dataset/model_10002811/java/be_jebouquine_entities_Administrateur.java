





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Administrateur  {

    private String emailAdministrateur;
    private String prenomAdministrateur;
    private String nomAdministrateur;
    private int idAdministrateur;
    private String motDePasseAdministrateur;



    public be_jebouquine_entities_Administrateur(
        String emailAdministrateur,        String prenomAdministrateur,        String nomAdministrateur,        int idAdministrateur,        String motDePasseAdministrateur    ) {
        this.emailAdministrateur = emailAdministrateur;
        this.prenomAdministrateur = prenomAdministrateur;
        this.nomAdministrateur = nomAdministrateur;
        this.idAdministrateur = idAdministrateur;
        this.motDePasseAdministrateur = motDePasseAdministrateur;
    }


    public String getEmailadministrateur() {
        return emailAdministrateur;
    }

    public void setEmailadministrateur(String emailAdministrateur) {
        this.emailAdministrateur = emailAdministrateur;
    }
    public String getPrenomadministrateur() {
        return prenomAdministrateur;
    }

    public void setPrenomadministrateur(String prenomAdministrateur) {
        this.prenomAdministrateur = prenomAdministrateur;
    }
    public String getNomadministrateur() {
        return nomAdministrateur;
    }

    public void setNomadministrateur(String nomAdministrateur) {
        this.nomAdministrateur = nomAdministrateur;
    }
    public int getIdadministrateur() {
        return idAdministrateur;
    }

    public void setIdadministrateur(int idAdministrateur) {
        this.idAdministrateur = idAdministrateur;
    }
    public String getMotdepasseadministrateur() {
        return motDePasseAdministrateur;
    }

    public void setMotdepasseadministrateur(String motDePasseAdministrateur) {
        this.motDePasseAdministrateur = motDePasseAdministrateur;
    }


}