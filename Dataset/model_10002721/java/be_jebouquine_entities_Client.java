





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Client  {

    private int idClient;
    private String adresseClient;
    private String etatLogin;
    private String motDePasseClient;
    private String telephoneClient;
    private String emailClient;
    private String nomClient;



    public be_jebouquine_entities_Client(
        int idClient,        String adresseClient,        String etatLogin,        String motDePasseClient,        String telephoneClient,        String emailClient,        String nomClient    ) {
        this.idClient = idClient;
        this.adresseClient = adresseClient;
        this.etatLogin = etatLogin;
        this.motDePasseClient = motDePasseClient;
        this.telephoneClient = telephoneClient;
        this.emailClient = emailClient;
        this.nomClient = nomClient;
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
    public String getEtatlogin() {
        return etatLogin;
    }

    public void setEtatlogin(String etatLogin) {
        this.etatLogin = etatLogin;
    }
    public String getMotdepasseclient() {
        return motDePasseClient;
    }

    public void setMotdepasseclient(String motDePasseClient) {
        this.motDePasseClient = motDePasseClient;
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
    public String getNomclient() {
        return nomClient;
    }

    public void setNomclient(String nomClient) {
        this.nomClient = nomClient;
    }


}