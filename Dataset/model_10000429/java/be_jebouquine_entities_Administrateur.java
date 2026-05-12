





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Administrateur  {

    private String nomAdministrateur;
    private String prenomAdministrateur;
    private String emailAdministrateur;
    private int idAdministrateur;
    private String motDePasseAdministrateur;



    public be_jebouquine_entities_Administrateur(
        String nomAdministrateur,        String prenomAdministrateur,        String emailAdministrateur,        int idAdministrateur,        String motDePasseAdministrateur    ) {
        this.nomAdministrateur = nomAdministrateur;
        this.prenomAdministrateur = prenomAdministrateur;
        this.emailAdministrateur = emailAdministrateur;
        this.idAdministrateur = idAdministrateur;
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
    public String getEmailadministrateur() {
        return emailAdministrateur;
    }

    public void setEmailadministrateur(String emailAdministrateur) {
        this.emailAdministrateur = emailAdministrateur;
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