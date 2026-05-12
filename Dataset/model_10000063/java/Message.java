





import java.util.List;
import java.util.ArrayList;

public class Message  {

    private String maxChars;





    private Utilisateur utilisateur;


    public Message(
        String maxChars    ) {
        this.maxChars = maxChars;
    }


    public String getMaxchars() {
        return maxChars;
    }

    public void setMaxchars(String maxChars) {
        this.maxChars = maxChars;
    }

    public Utilisateur getUtilisateur() {
        return utilisateur;
    }

    public void setUtilisateur(Utilisateur utilisateur) {
        this.utilisateur = utilisateur;
    }

}