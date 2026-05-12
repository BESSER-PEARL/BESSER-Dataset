





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Client  {

    private String adresseClient;
    private String motDePasseClient;
    private String etatLogin;
    private String nomClient;
    private int idClient;
    private String telephoneClient;
    private String emailClient;





    private List<be_jebouquine_entities_Commentaire> be_jebouquine_entities_commentaires;


    public be_jebouquine_entities_Client(
        String adresseClient,        String motDePasseClient,        String etatLogin,        String nomClient,        int idClient,        String telephoneClient,        String emailClient    ) {
        this.adresseClient = adresseClient;
        this.motDePasseClient = motDePasseClient;
        this.etatLogin = etatLogin;
        this.nomClient = nomClient;
        this.idClient = idClient;
        this.telephoneClient = telephoneClient;
        this.emailClient = emailClient;
        this.be_jebouquine_entities_commentaires = new ArrayList<>();
    }

    public be_jebouquine_entities_Client(
        String adresseClient,        String motDePasseClient,        String etatLogin,        String nomClient,        int idClient,        String telephoneClient,        String emailClient        ArrayList<be_jebouquine_entities_Commentaire> be_jebouquine_entities_commentaires    ) {
        this.adresseClient = adresseClient;
        this.motDePasseClient = motDePasseClient;
        this.etatLogin = etatLogin;
        this.nomClient = nomClient;
        this.idClient = idClient;
        this.telephoneClient = telephoneClient;
        this.emailClient = emailClient;
        this.be_jebouquine_entities_commentaires = be_jebouquine_entities_commentaires;
    }

    public String getAdresseclient() {
        return adresseClient;
    }

    public void setAdresseclient(String adresseClient) {
        this.adresseClient = adresseClient;
    }
    public String getMotdepasseclient() {
        return motDePasseClient;
    }

    public void setMotdepasseclient(String motDePasseClient) {
        this.motDePasseClient = motDePasseClient;
    }
    public String getEtatlogin() {
        return etatLogin;
    }

    public void setEtatlogin(String etatLogin) {
        this.etatLogin = etatLogin;
    }
    public String getNomclient() {
        return nomClient;
    }

    public void setNomclient(String nomClient) {
        this.nomClient = nomClient;
    }
    public int getIdclient() {
        return idClient;
    }

    public void setIdclient(int idClient) {
        this.idClient = idClient;
    }
    public String getTelephoneclient() {
        return telephoneClient;
    }

    public void setTelephoneclient(String telephoneClient) {
        this.telephoneClient = telephoneClient;
    }
    public String getEmailclient() {
        return emailClient;
    }

    public void setEmailclient(String emailClient) {
        this.emailClient = emailClient;
    }

    public List<be_jebouquine_entities_Commentaire> getBe_jebouquine_entities_commentaires() {
        return be_jebouquine_entities_commentaires;
    }

    public void addBe_jebouquine_entities_commentaire(Be_jebouquine_entities_commentaire be_jebouquine_entities_commentaire) {
        this.be_jebouquine_entities_commentaires.add(be_jebouquine_entities_commentaire);
    }

}