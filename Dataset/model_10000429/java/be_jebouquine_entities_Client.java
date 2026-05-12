





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Client  {

    private String motDePasseClient;
    private String emailClient;
    private String telephoneClient;
    private String etatLogin;
    private int idClient;
    private String adresseClient;
    private String nomClient;



    public be_jebouquine_entities_Client(
        String motDePasseClient,        String emailClient,        String telephoneClient,        String etatLogin,        int idClient,        String adresseClient,        String nomClient    ) {
        this.motDePasseClient = motDePasseClient;
        this.emailClient = emailClient;
        this.telephoneClient = telephoneClient;
        this.etatLogin = etatLogin;
        this.idClient = idClient;
        this.adresseClient = adresseClient;
        this.nomClient = nomClient;
    }


    public String getMotdepasseclient() {
        return motDePasseClient;
    }

    public void setMotdepasseclient(String motDePasseClient) {
        this.motDePasseClient = motDePasseClient;
    }
    public String getEmailclient() {
        return emailClient;
    }

    public void setEmailclient(String emailClient) {
        this.emailClient = emailClient;
    }
    public String getTelephoneclient() {
        return telephoneClient;
    }

    public void setTelephoneclient(String telephoneClient) {
        this.telephoneClient = telephoneClient;
    }
    public String getEtatlogin() {
        return etatLogin;
    }

    public void setEtatlogin(String etatLogin) {
        this.etatLogin = etatLogin;
    }
    public int getIdclient() {
        return idClient;
    }

    public void setIdclient(int idClient) {
        this.idClient = idClient;
    }
    public String getAdresseclient() {
        return adresseClient;
    }

    public void setAdresseclient(String adresseClient) {
        this.adresseClient = adresseClient;
    }
    public String getNomclient() {
        return nomClient;
    }

    public void setNomclient(String nomClient) {
        this.nomClient = nomClient;
    }


}