





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Administrateur  {

    private int idAdministrateur;
    private String emailAdministrateur;
    private String motDePasseAdministrateur;
    private String nomAdministrateur;
    private String prenomAdministrateur;



    public be_jebouquine_entities_Administrateur(
        int idAdministrateur,        String emailAdministrateur,        String motDePasseAdministrateur,        String nomAdministrateur,        String prenomAdministrateur    ) {
        this.idAdministrateur = idAdministrateur;
        this.emailAdministrateur = emailAdministrateur;
        this.motDePasseAdministrateur = motDePasseAdministrateur;
        this.nomAdministrateur = nomAdministrateur;
        this.prenomAdministrateur = prenomAdministrateur;
    }


    public int getIdadministrateur() {
        return idAdministrateur;
    }

    public void setIdadministrateur(int idAdministrateur) {
        this.idAdministrateur = idAdministrateur;
    }
    public String getEmailadministrateur() {
        return emailAdministrateur;
    }

    public void setEmailadministrateur(String emailAdministrateur) {
        this.emailAdministrateur = emailAdministrateur;
    }
    public String getMotdepasseadministrateur() {
        return motDePasseAdministrateur;
    }

    public void setMotdepasseadministrateur(String motDePasseAdministrateur) {
        this.motDePasseAdministrateur = motDePasseAdministrateur;
    }
    public String getNomadministrateur() {
        return nomAdministrateur;
    }

    public void setNomadministrateur(String nomAdministrateur) {
        this.nomAdministrateur = nomAdministrateur;
    }
    public String getPrenomadministrateur() {
        return prenomAdministrateur;
    }

    public void setPrenomadministrateur(String prenomAdministrateur) {
        this.prenomAdministrateur = prenomAdministrateur;
    }


}