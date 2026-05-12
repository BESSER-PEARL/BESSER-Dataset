





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Administrateur  {

    private String emailAdministrateur;
    private String nomAdministrateur;
    private String prenomAdministrateur;
    private String motDePasseAdministrateur;
    private int idAdministrateur;



    public be_jebouquine_entities_Administrateur(
        String emailAdministrateur,        String nomAdministrateur,        String prenomAdministrateur,        String motDePasseAdministrateur,        int idAdministrateur    ) {
        this.emailAdministrateur = emailAdministrateur;
        this.nomAdministrateur = nomAdministrateur;
        this.prenomAdministrateur = prenomAdministrateur;
        this.motDePasseAdministrateur = motDePasseAdministrateur;
        this.idAdministrateur = idAdministrateur;
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
    public String getPrenomadministrateur() {
        return prenomAdministrateur;
    }

    public void setPrenomadministrateur(String prenomAdministrateur) {
        this.prenomAdministrateur = prenomAdministrateur;
    }
    public String getMotdepasseadministrateur() {
        return motDePasseAdministrateur;
    }

    public void setMotdepasseadministrateur(String motDePasseAdministrateur) {
        this.motDePasseAdministrateur = motDePasseAdministrateur;
    }
    public int getIdadministrateur() {
        return idAdministrateur;
    }

    public void setIdadministrateur(int idAdministrateur) {
        this.idAdministrateur = idAdministrateur;
    }


}