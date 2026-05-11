





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_Model  {






    private List<applauseDsl_ModelElement> applausedsl_modelelements;


    public applauseDsl_Model(
    ) {
        this.applausedsl_modelelements = new ArrayList<>();
    }

    public applauseDsl_Model(
        ArrayList<applauseDsl_ModelElement> applausedsl_modelelements    ) {
        this.applausedsl_modelelements = applausedsl_modelelements;
    }


    public List<applauseDsl_ModelElement> getApplausedsl_modelelements() {
        return applausedsl_modelelements;
    }

    public void addApplausedsl_modelelement(Applausedsl_modelelement applausedsl_modelelement) {
        this.applausedsl_modelelements.add(applausedsl_modelelement);
    }

}