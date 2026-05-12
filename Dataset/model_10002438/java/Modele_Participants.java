





import java.util.List;
import java.util.ArrayList;

public class Modele_Participants  {

    private int NOMBRE;
    private String attribute;





    private List<Modele_Joueur> modele_joueurs;


    public Modele_Participants(
        int NOMBRE,        String attribute    ) {
        this.NOMBRE = NOMBRE;
        this.attribute = attribute;
        this.modele_joueurs = new ArrayList<>();
    }

    public Modele_Participants(
        int NOMBRE,        String attribute        ArrayList<Modele_Joueur> modele_joueurs    ) {
        this.NOMBRE = NOMBRE;
        this.attribute = attribute;
        this.modele_joueurs = modele_joueurs;
    }

    public int getNombre() {
        return NOMBRE;
    }

    public void setNombre(int NOMBRE) {
        this.NOMBRE = NOMBRE;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }

    public List<Modele_Joueur> getModele_joueurs() {
        return modele_joueurs;
    }

    public void addModele_joueur(Modele_joueur modele_joueur) {
        this.modele_joueurs.add(modele_joueur);
    }

}