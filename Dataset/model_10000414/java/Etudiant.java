





import java.util.List;
import java.util.ArrayList;

public class Etudiant  {

    private float list_notes;
    private boolean actif;
    private String cv;
    private String list_commentaire;
    private int id_etudiant;





    private List<Personne> personnes;


    public Etudiant(
        float list_notes,        boolean actif,        String cv,        String list_commentaire,        int id_etudiant    ) {
        this.list_notes = list_notes;
        this.actif = actif;
        this.cv = cv;
        this.list_commentaire = list_commentaire;
        this.id_etudiant = id_etudiant;
        this.personnes = new ArrayList<>();
    }

    public Etudiant(
        float list_notes,        boolean actif,        String cv,        String list_commentaire,        int id_etudiant        ArrayList<Personne> personnes    ) {
        this.list_notes = list_notes;
        this.actif = actif;
        this.cv = cv;
        this.list_commentaire = list_commentaire;
        this.id_etudiant = id_etudiant;
        this.personnes = personnes;
    }

    public float getList_notes() {
        return list_notes;
    }

    public void setList_notes(float list_notes) {
        this.list_notes = list_notes;
    }
    public boolean getActif() {
        return actif;
    }

    public void setActif(boolean actif) {
        this.actif = actif;
    }
    public String getCv() {
        return cv;
    }

    public void setCv(String cv) {
        this.cv = cv;
    }
    public String getList_commentaire() {
        return list_commentaire;
    }

    public void setList_commentaire(String list_commentaire) {
        this.list_commentaire = list_commentaire;
    }
    public int getId_etudiant() {
        return id_etudiant;
    }

    public void setId_etudiant(int id_etudiant) {
        this.id_etudiant = id_etudiant;
    }

    public List<Personne> getPersonnes() {
        return personnes;
    }

    public void addPersonne(Personne personne) {
        this.personnes.add(personne);
    }

}