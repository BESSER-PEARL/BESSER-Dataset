





import java.util.List;
import java.util.ArrayList;

public class Role  {

    private int nbAvis;





    private Utilisateur2 utilisateur2;




    private List<Avis2> avis2s;


    public Role(
        int nbAvis    ) {
        this.nbAvis = nbAvis;
        this.avis2s = new ArrayList<>();
    }

    public Role(
        int nbAvis        ArrayList<Avis2> avis2s    ) {
        this.nbAvis = nbAvis;
        this.avis2s = avis2s;
    }

    public int getNbavis() {
        return nbAvis;
    }

    public void setNbavis(int nbAvis) {
        this.nbAvis = nbAvis;
    }

    public Utilisateur2 getUtilisateur2() {
        return utilisateur2;
    }

    public void setUtilisateur2(Utilisateur2 utilisateur2) {
        this.utilisateur2 = utilisateur2;
    }
    public List<Avis2> getAvis2s() {
        return avis2s;
    }

    public void addAvis2(Avis2 avis2) {
        this.avis2s.add(avis2);
    }

}