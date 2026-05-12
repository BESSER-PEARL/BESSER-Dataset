





import java.util.List;
import java.util.ArrayList;

public class Group  {

    private String discription;
    private String name;





    private Utilisateur utilisateur;


    public Group(
        String discription,        String name    ) {
        this.discription = discription;
        this.name = name;
    }


    public String getDiscription() {
        return discription;
    }

    public void setDiscription(String discription) {
        this.discription = discription;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }

}