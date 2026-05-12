





import java.util.List;
import java.util.ArrayList;

public class Analyse_Criteres  {

    private int qualit_;
    private int amabilite;
    private int rapidite;
    private int respectHoraires;
    private int rapportQualitePrix;





    private List<Analyse_Review> analyse_reviews;


    public Analyse_Criteres(
        int qualit_,        int amabilite,        int rapidite,        int respectHoraires,        int rapportQualitePrix    ) {
        this.qualit_ = qualit_;
        this.amabilite = amabilite;
        this.rapidite = rapidite;
        this.respectHoraires = respectHoraires;
        this.rapportQualitePrix = rapportQualitePrix;
        this.analyse_reviews = new ArrayList<>();
    }

    public Analyse_Criteres(
        int qualit_,        int amabilite,        int rapidite,        int respectHoraires,        int rapportQualitePrix        ArrayList<Analyse_Review> analyse_reviews    ) {
        this.qualit_ = qualit_;
        this.amabilite = amabilite;
        this.rapidite = rapidite;
        this.respectHoraires = respectHoraires;
        this.rapportQualitePrix = rapportQualitePrix;
        this.analyse_reviews = analyse_reviews;
    }

    public int getQualit_() {
        return qualit_;
    }

    public void setQualit_(int qualit_) {
        this.qualit_ = qualit_;
    }
    public int getAmabilite() {
        return amabilite;
    }

    public void setAmabilite(int amabilite) {
        this.amabilite = amabilite;
    }
    public int getRapidite() {
        return rapidite;
    }

    public void setRapidite(int rapidite) {
        this.rapidite = rapidite;
    }
    public int getRespecthoraires() {
        return respectHoraires;
    }

    public void setRespecthoraires(int respectHoraires) {
        this.respectHoraires = respectHoraires;
    }
    public int getRapportqualiteprix() {
        return rapportQualitePrix;
    }

    public void setRapportqualiteprix(int rapportQualitePrix) {
        this.rapportQualitePrix = rapportQualitePrix;
    }

    public List<Analyse_Review> getAnalyse_reviews() {
        return analyse_reviews;
    }

    public void addAnalyse_review(Analyse_review analyse_review) {
        this.analyse_reviews.add(analyse_review);
    }

}