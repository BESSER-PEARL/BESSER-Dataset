





import java.util.List;
import java.util.ArrayList;

public class CompteDeLUtilisateur1  {

    private String peudo;
    private String adresseMail;
    private String motDePasse;
    private String Type;



    public CompteDeLUtilisateur1(
        String peudo,        String adresseMail,        String motDePasse,        String Type    ) {
        this.peudo = peudo;
        this.adresseMail = adresseMail;
        this.motDePasse = motDePasse;
        this.Type = Type;
    }


    public String getPeudo() {
        return peudo;
    }

    public void setPeudo(String peudo) {
        this.peudo = peudo;
    }
    public String getAdressemail() {
        return adresseMail;
    }

    public void setAdressemail(String adresseMail) {
        this.adresseMail = adresseMail;
    }
    public String getMotdepasse() {
        return motDePasse;
    }

    public void setMotdepasse(String motDePasse) {
        this.motDePasse = motDePasse;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }


}