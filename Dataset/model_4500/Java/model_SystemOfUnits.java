





import java.util.List;
import java.util.ArrayList;

public class model_SystemOfUnits  {

    private String name;
    private String standardizationBody;





    private List<model_Unit> model_units;


    public model_SystemOfUnits(
        String name,        String standardizationBody    ) {
        this.name = name;
        this.standardizationBody = standardizationBody;
        this.model_units = new ArrayList<>();
    }

    public model_SystemOfUnits(
        String name,        String standardizationBody        ArrayList<model_Unit> model_units    ) {
        this.name = name;
        this.standardizationBody = standardizationBody;
        this.model_units = model_units;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getStandardizationbody() {
        return standardizationBody;
    }

    public void setStandardizationbody(String standardizationBody) {
        this.standardizationBody = standardizationBody;
    }

    public List<model_Unit> getModel_units() {
        return model_units;
    }

    public void addModel_unit(Model_unit model_unit) {
        this.model_units.add(model_unit);
    }

}