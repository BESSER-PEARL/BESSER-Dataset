





import java.util.List;
import java.util.ArrayList;

public class Analyse2_Criteres  {

    private int amabilite;
    private int rapidite;
    private int respectHoraires;
    private int qualit_;
    private int rapportQualitePrix;





    private List<Analyse2_Review> analyse2_reviews;


    public Analyse2_Criteres(
        int amabilite,        int rapidite,        int respectHoraires,        int qualit_,        int rapportQualitePrix    ) {
        this.amabilite = amabilite;
        this.rapidite = rapidite;
        this.respectHoraires = respectHoraires;
        this.qualit_ = qualit_;
        this.rapportQualitePrix = rapportQualitePrix;
        this.analyse2_reviews = new ArrayList<>();
    }

    public Analyse2_Criteres(
        int amabilite,        int rapidite,        int respectHoraires,        int qualit_,        int rapportQualitePrix        ArrayList<Analyse2_Review> analyse2_reviews    ) {
        this.amabilite = amabilite;
        this.rapidite = rapidite;
        this.respectHoraires = respectHoraires;
        this.qualit_ = qualit_;
        this.rapportQualitePrix = rapportQualitePrix;
        this.analyse2_reviews = analyse2_reviews;
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
    public int getQualit_() {
        return qualit_;
    }

    public void setQualit_(int qualit_) {
        this.qualit_ = qualit_;
    }
    public int getRapportqualiteprix() {
        return rapportQualitePrix;
    }

    public void setRapportqualiteprix(int rapportQualitePrix) {
        this.rapportQualitePrix = rapportQualitePrix;
    }

    public List<Analyse2_Review> getAnalyse2_reviews() {
        return analyse2_reviews;
    }

    public void addAnalyse2_review(Analyse2_review analyse2_review) {
        this.analyse2_reviews.add(analyse2_review);
    }

}