





import java.util.List;
import java.util.ArrayList;

public class CHAUFFEUR  {

    private String nomPersonnel;
    private String prenomPersonnel;





    private List<PERMIS> permiss;


    public CHAUFFEUR(
        String nomPersonnel,        String prenomPersonnel    ) {
        this.nomPersonnel = nomPersonnel;
        this.prenomPersonnel = prenomPersonnel;
        this.permiss = new ArrayList<>();
    }

    public CHAUFFEUR(
        String nomPersonnel,        String prenomPersonnel        ArrayList<PERMIS> permiss    ) {
        this.nomPersonnel = nomPersonnel;
        this.prenomPersonnel = prenomPersonnel;
        this.permiss = permiss;
    }

    public String getNompersonnel() {
        return nomPersonnel;
    }

    public void setNompersonnel(String nomPersonnel) {
        this.nomPersonnel = nomPersonnel;
    }
    public String getPrenompersonnel() {
        return prenomPersonnel;
    }

    public void setPrenompersonnel(String prenomPersonnel) {
        this.prenomPersonnel = prenomPersonnel;
    }

    public List<PERMIS> getPermiss() {
        return permiss;
    }

    public void addPermis(Permis permis) {
        this.permiss.add(permis);
    }

}