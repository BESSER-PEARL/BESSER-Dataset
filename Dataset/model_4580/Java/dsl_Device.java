





import java.util.List;
import java.util.ArrayList;

public class dsl_Device  {

    private String name;





    private List<dsl_Fonctionnalite> dsl_fonctionnalites;


    public dsl_Device(
        String name    ) {
        this.name = name;
        this.dsl_fonctionnalites = new ArrayList<>();
    }

    public dsl_Device(
        String name        ArrayList<dsl_Fonctionnalite> dsl_fonctionnalites    ) {
        this.name = name;
        this.dsl_fonctionnalites = dsl_fonctionnalites;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<dsl_Fonctionnalite> getDsl_fonctionnalites() {
        return dsl_fonctionnalites;
    }

    public void addDsl_fonctionnalite(Dsl_fonctionnalite dsl_fonctionnalite) {
        this.dsl_fonctionnalites.add(dsl_fonctionnalite);
    }

}