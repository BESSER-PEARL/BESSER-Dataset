





import java.util.List;
import java.util.ArrayList;

public class dsl_Parametre  {

    private String name;





    private dsl_Fonctionnalite dsl_fonctionnalite;


    public dsl_Parametre(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Fonctionnalite getDsl_fonctionnalite() {
        return dsl_fonctionnalite;
    }

    public void setDsl_fonctionnalite(dsl_Fonctionnalite dsl_fonctionnalite) {
        this.dsl_fonctionnalite = dsl_fonctionnalite;
    }

}