





import java.util.List;
import java.util.ArrayList;

public class Modele_Participants  {

    private String attribute;
    private int NOMBRE;





    private List<Modele_Joueur> modele_joueurs;


    public Modele_Participants(
        String attribute,        int NOMBRE    ) {
        this.attribute = attribute;
        this.NOMBRE = NOMBRE;
        this.modele_joueurs = new ArrayList<>();
    }

    public Modele_Participants(
        String attribute,        int NOMBRE        ArrayList<Modele_Joueur> modele_joueurs    ) {
        this.attribute = attribute;
        this.NOMBRE = NOMBRE;
        this.modele_joueurs = modele_joueurs;
    }

    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public int getNombre() {
        return NOMBRE;
    }

    public void setNombre(int NOMBRE) {
        this.NOMBRE = NOMBRE;
    }

    public List<Modele_Joueur> getModele_joueurs() {
        return modele_joueurs;
    }

    public void addModele_joueur(Modele_joueur modele_joueur) {
        this.modele_joueurs.add(modele_joueur);
    }

}