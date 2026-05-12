





import java.util.List;
import java.util.ArrayList;

public class covoiturage_Preferences  {

    private String valeur;
    private int id;
    private String nomPref;





    private List<covoiturage_Personne> covoiturage_personnes;


    public covoiturage_Preferences(
        String valeur,        int id,        String nomPref    ) {
        this.valeur = valeur;
        this.id = id;
        this.nomPref = nomPref;
        this.covoiturage_personnes = new ArrayList<>();
    }

    public covoiturage_Preferences(
        String valeur,        int id,        String nomPref        ArrayList<covoiturage_Personne> covoiturage_personnes    ) {
        this.valeur = valeur;
        this.id = id;
        this.nomPref = nomPref;
        this.covoiturage_personnes = covoiturage_personnes;
    }

    public String getValeur() {
        return valeur;
    }

    public void setValeur(String valeur) {
        this.valeur = valeur;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getNompref() {
        return nomPref;
    }

    public void setNompref(String nomPref) {
        this.nomPref = nomPref;
    }

    public List<covoiturage_Personne> getCovoiturage_personnes() {
        return covoiturage_personnes;
    }

    public void addCovoiturage_personne(Covoiturage_personne covoiturage_personne) {
        this.covoiturage_personnes.add(covoiturage_personne);
    }

}