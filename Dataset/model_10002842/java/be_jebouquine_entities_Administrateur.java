





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Administrateur  {

    private String motDePasseAdministrateur;
    private String emailAdministrateur;
    private String nomAdministrateur;
    private int idAdministrateur;
    private String prenomAdministrateur;



    public be_jebouquine_entities_Administrateur(
        String motDePasseAdministrateur,        String emailAdministrateur,        String nomAdministrateur,        int idAdministrateur,        String prenomAdministrateur    ) {
        this.motDePasseAdministrateur = motDePasseAdministrateur;
        this.emailAdministrateur = emailAdministrateur;
        this.nomAdministrateur = nomAdministrateur;
        this.idAdministrateur = idAdministrateur;
        this.prenomAdministrateur = prenomAdministrateur;
    }


    public String getMotdepasseadministrateur() {
        return motDePasseAdministrateur;
    }

    public void setMotdepasseadministrateur(String motDePasseAdministrateur) {
        this.motDePasseAdministrateur = motDePasseAdministrateur;
    }
    public String getEmailadministrateur() {
        return emailAdministrateur;
    }

    public void setEmailadministrateur(String emailAdministrateur) {
        this.emailAdministrateur = emailAdministrateur;
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
    public String getPrenomadministrateur() {
        return prenomAdministrateur;
    }

    public void setPrenomadministrateur(String prenomAdministrateur) {
        this.prenomAdministrateur = prenomAdministrateur;
    }


}