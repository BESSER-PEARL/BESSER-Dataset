





import java.util.List;
import java.util.ArrayList;

public class CompteDeLUtilisateur  {

    private String peudo;
    private String motDePasse;
    private String adresseMail;
    private String Type;



    public CompteDeLUtilisateur(
        String peudo,        String motDePasse,        String adresseMail,        String Type    ) {
        this.peudo = peudo;
        this.motDePasse = motDePasse;
        this.adresseMail = adresseMail;
        this.Type = Type;
    }


    public String getPeudo() {
        return peudo;
    }

    public void setPeudo(String peudo) {
        this.peudo = peudo;
    }
    public String getMotdepasse() {
        return motDePasse;
    }

    public void setMotdepasse(String motDePasse) {
        this.motDePasse = motDePasse;
    }
    public String getAdressemail() {
        return adresseMail;
    }

    public void setAdressemail(String adresseMail) {
        this.adresseMail = adresseMail;
    }
    public String getType() {
        return Type;
    }

    public void setType(String Type) {
        this.Type = Type;
    }


}