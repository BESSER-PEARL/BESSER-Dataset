





import java.util.List;
import java.util.ArrayList;

public class dslComponent_Subsystem  {

    private String description;
    private String name;





    private dslComponent_WTComponents dslcomponent_wtcomponents;




    private List<dslComponent_Subsystem> dslcomponent_subsystems;


    public dslComponent_Subsystem(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.dslcomponent_subsystems = new ArrayList<>();
    }

    public dslComponent_Subsystem(
        String description,        String name        ArrayList<dslComponent_Subsystem> dslcomponent_subsystems    ) {
        this.description = description;
        this.name = name;
        this.dslcomponent_subsystems = dslcomponent_subsystems;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dslComponent_WTComponents getDslcomponent_wtcomponents() {
        return dslcomponent_wtcomponents;
    }

    public void setDslcomponent_wtcomponents(dslComponent_WTComponents dslcomponent_wtcomponents) {
        this.dslcomponent_wtcomponents = dslcomponent_wtcomponents;
    }
    public List<dslComponent_Subsystem> getDslcomponent_subsystems() {
        return dslcomponent_subsystems;
    }

    public void addDslcomponent_subsystem(Dslcomponent_subsystem dslcomponent_subsystem) {
        this.dslcomponent_subsystems.add(dslcomponent_subsystem);
    }

}