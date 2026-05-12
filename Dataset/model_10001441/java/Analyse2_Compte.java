





import java.util.List;
import java.util.ArrayList;

public class Analyse2_Compte  {

    private String motdepasse;
    private String login;





    private List<Analyse2_Review> analyse2_reviews;




    private Analyse2_Utilisateur analyse2_utilisateur;


    public Analyse2_Compte(
        String motdepasse,        String login    ) {
        this.motdepasse = motdepasse;
        this.login = login;
        this.analyse2_reviews = new ArrayList<>();
    }

    public Analyse2_Compte(
        String motdepasse,        String login        ArrayList<Analyse2_Review> analyse2_reviews    ) {
        this.motdepasse = motdepasse;
        this.login = login;
        this.analyse2_reviews = analyse2_reviews;
    }

    public String getMotdepasse() {
        return motdepasse;
    }

    public void setMotdepasse(String motdepasse) {
        this.motdepasse = motdepasse;
    }
    public String getLogin() {
        return login;
    }

    public void setLogin(String login) {
        this.login = login;
    }

    public List<Analyse2_Review> getAnalyse2_reviews() {
        return analyse2_reviews;
    }

    public void addAnalyse2_review(Analyse2_review analyse2_review) {
        this.analyse2_reviews.add(analyse2_review);
    }
    public Analyse2_Utilisateur getAnalyse2_utilisateur() {
        return analyse2_utilisateur;
    }

    public void setAnalyse2_utilisateur(Analyse2_Utilisateur analyse2_utilisateur) {
        this.analyse2_utilisateur = analyse2_utilisateur;
    }

}