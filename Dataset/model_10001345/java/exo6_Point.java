





import java.util.List;
import java.util.ArrayList;

public class exo6_Point  {

    private None abcisse;
    private None ordonnee;





    private List<exo6_Polygone> exo6_polygones;


    public exo6_Point(
        None abcisse,        None ordonnee    ) {
        this.abcisse = abcisse;
        this.ordonnee = ordonnee;
        this.exo6_polygones = new ArrayList<>();
    }

    public exo6_Point(
        None abcisse,        None ordonnee        ArrayList<exo6_Polygone> exo6_polygones    ) {
        this.abcisse = abcisse;
        this.ordonnee = ordonnee;
        this.exo6_polygones = exo6_polygones;
    }

    public None getAbcisse() {
        return abcisse;
    }

    public void setAbcisse(None abcisse) {
        this.abcisse = abcisse;
    }
    public None getOrdonnee() {
        return ordonnee;
    }

    public void setOrdonnee(None ordonnee) {
        this.ordonnee = ordonnee;
    }

    public List<exo6_Polygone> getExo6_polygones() {
        return exo6_polygones;
    }

    public void addExo6_polygone(Exo6_polygone exo6_polygone) {
        this.exo6_polygones.add(exo6_polygone);
    }

}