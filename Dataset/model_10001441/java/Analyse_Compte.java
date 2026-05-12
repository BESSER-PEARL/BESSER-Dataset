





import java.util.List;
import java.util.ArrayList;

public class Analyse_Compte  {

    private String motdepasse;
    private String login;





    private List<Analyse_Review> analyse_reviews;




    private Analyse_Utilisateur analyse_utilisateur;


    public Analyse_Compte(
        String motdepasse,        String login    ) {
        this.motdepasse = motdepasse;
        this.login = login;
        this.analyse_reviews = new ArrayList<>();
    }

    public Analyse_Compte(
        String motdepasse,        String login        ArrayList<Analyse_Review> analyse_reviews    ) {
        this.motdepasse = motdepasse;
        this.login = login;
        this.analyse_reviews = analyse_reviews;
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

    public List<Analyse_Review> getAnalyse_reviews() {
        return analyse_reviews;
    }

    public void addAnalyse_review(Analyse_review analyse_review) {
        this.analyse_reviews.add(analyse_review);
    }
    public Analyse_Utilisateur getAnalyse_utilisateur() {
        return analyse_utilisateur;
    }

    public void setAnalyse_utilisateur(Analyse_Utilisateur analyse_utilisateur) {
        this.analyse_utilisateur = analyse_utilisateur;
    }

}