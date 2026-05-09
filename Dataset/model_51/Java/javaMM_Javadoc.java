





import java.util.List;
import java.util.ArrayList;

public class javaMM_Javadoc extends Comment {






    private List<javaMM_TagElement> javamm_tagelements;


    public javaMM_Javadoc(
    ) {
        super(
        );
        this.javamm_tagelements = new ArrayList<>();
    }

    public javaMM_Javadoc(
        ArrayList<javaMM_TagElement> javamm_tagelements    ) {
        this.javamm_tagelements = javamm_tagelements;
    }


    public List<javaMM_TagElement> getJavamm_tagelements() {
        return javamm_tagelements;
    }

    public void addJavamm_tagelement(Javamm_tagelement javamm_tagelement) {
        this.javamm_tagelements.add(javamm_tagelement);
    }

}