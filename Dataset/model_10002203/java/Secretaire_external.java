





import java.util.List;
import java.util.ArrayList;

public class Secretaire_external  {






    private List<ResultatExamen> resultatexamens;


    public Secretaire_external(
    ) {
        this.resultatexamens = new ArrayList<>();
    }

    public Secretaire_external(
        ArrayList<ResultatExamen> resultatexamens    ) {
        this.resultatexamens = resultatexamens;
    }


    public List<ResultatExamen> getResultatexamens() {
        return resultatexamens;
    }

    public void addResultatexamen(Resultatexamen resultatexamen) {
        this.resultatexamens.add(resultatexamen);
    }

}