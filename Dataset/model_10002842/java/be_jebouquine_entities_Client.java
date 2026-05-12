





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Client  {

    private int idClient;
    private String telephoneClient;
    private String etatLogin;
    private String emailClient;
    private String adresseClient;
    private String nomClient;
    private String motDePasseClient;



    public be_jebouquine_entities_Client(
        int idClient,        String telephoneClient,        String etatLogin,        String emailClient,        String adresseClient,        String nomClient,        String motDePasseClient    ) {
        this.idClient = idClient;
        this.telephoneClient = telephoneClient;
        this.etatLogin = etatLogin;
        this.emailClient = emailClient;
        this.adresseClient = adresseClient;
        this.nomClient = nomClient;
        this.motDePasseClient = motDePasseClient;
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
    public String getEtatlogin() {
        return etatLogin;
    }

    public void setEtatlogin(String etatLogin) {
        this.etatLogin = etatLogin;
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


}