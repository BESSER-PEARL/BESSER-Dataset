





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Client  {

    private String etatLogin;
    private String nomClient;
    private String motDePasseClient;
    private String adresseClient;
    private int idClient;
    private String telephoneClient;
    private String emailClient;



    public be_jebouquine_entities_Client(
        String etatLogin,        String nomClient,        String motDePasseClient,        String adresseClient,        int idClient,        String telephoneClient,        String emailClient    ) {
        this.etatLogin = etatLogin;
        this.nomClient = nomClient;
        this.motDePasseClient = motDePasseClient;
        this.adresseClient = adresseClient;
        this.idClient = idClient;
        this.telephoneClient = telephoneClient;
        this.emailClient = emailClient;
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
    public String getMotdepasseclient() {
        return motDePasseClient;
    }

    public void setMotdepasseclient(String motDePasseClient) {
        this.motDePasseClient = motDePasseClient;
    }
    public String getAdresseclient() {
        return adresseClient;
    }

    public void setAdresseclient(String adresseClient) {
        this.adresseClient = adresseClient;
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


}