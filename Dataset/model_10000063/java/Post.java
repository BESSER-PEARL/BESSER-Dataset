





import java.util.List;
import java.util.ArrayList;

public class Post  {

    private String privacy;
    private String info;





    private Utilisateur utilisateur;


    public Post(
        String privacy,        String info    ) {
        this.privacy = privacy;
        this.info = info;
    }


    public String getPrivacy() {
        return privacy;
    }

    public void setPrivacy(String privacy) {
        this.privacy = privacy;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }

    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }

}