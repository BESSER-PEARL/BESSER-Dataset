





import java.util.List;
import java.util.ArrayList;

public class morel_Executable  {

    private boolean active;
    private String parameters;





    private List<morel_PrimitiveVariable> morel_primitivevariables;


    public morel_Executable(
        boolean active,        String parameters    ) {
        this.active = active;
        this.parameters = parameters;
        this.morel_primitivevariables = new ArrayList<>();
    }

    public morel_Executable(
        boolean active,        String parameters        ArrayList<morel_PrimitiveVariable> morel_primitivevariables    ) {
        this.active = active;
        this.parameters = parameters;
        this.morel_primitivevariables = morel_primitivevariables;
    }

    public boolean getActive() {
        return active;
    }

    public void setActive(boolean active) {
        this.active = active;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }

    public List<morel_PrimitiveVariable> getMorel_primitivevariables() {
        return morel_primitivevariables;
    }

    public void addMorel_primitivevariable(Morel_primitivevariable morel_primitivevariable) {
        this.morel_primitivevariables.add(morel_primitivevariable);
    }

}