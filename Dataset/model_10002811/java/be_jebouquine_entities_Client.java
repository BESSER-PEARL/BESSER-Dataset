





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Client  {

    private int idClient;
    private String etatLogin;
    private String nomClient;
    private String emailClient;
    private String adresseClient;
    private String motDePasseClient;
    private String telephoneClient;



    public be_jebouquine_entities_Client(
        int idClient,        String etatLogin,        String nomClient,        String emailClient,        String adresseClient,        String motDePasseClient,        String telephoneClient    ) {
        this.idClient = idClient;
        this.etatLogin = etatLogin;
        this.nomClient = nomClient;
        this.emailClient = emailClient;
        this.adresseClient = adresseClient;
        this.motDePasseClient = motDePasseClient;
        this.telephoneClient = telephoneClient;
    }


    public int getIdclient() {
        return idClient;
    }

    public void setIdclient(int idClient) {
        this.idClient = idClient;
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
    public String getEmailclient() {
        return emailClient;
    }

    public void setEmailclient(String emailClient) {
        this.emailClient = emailClient;
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
    public String getTelephoneclient() {
        return telephoneClient;
    }

    public void setTelephoneclient(String telephoneClient) {
        this.telephoneClient = telephoneClient;
    }


}