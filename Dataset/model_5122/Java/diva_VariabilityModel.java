





import java.util.List;
import java.util.ArrayList;

public class diva_VariabilityModel  {






    private List<diva_Dimension> diva_dimensions;




    private List<diva_Property> diva_propertys;




    private List<diva_Variable> diva_variables;


    public diva_VariabilityModel(
    ) {
        this.diva_dimensions = new ArrayList<>();
        this.diva_propertys = new ArrayList<>();
        this.diva_variables = new ArrayList<>();
    }

    public diva_VariabilityModel(
        ArrayList<diva_Dimension> diva_dimensions,        ArrayList<diva_Property> diva_propertys,        ArrayList<diva_Variable> diva_variables    ) {
        this.diva_dimensions = diva_dimensions;
        this.diva_propertys = diva_propertys;
        this.diva_variables = diva_variables;
    }


    public List<diva_Dimension> getDiva_dimensions() {
        return diva_dimensions;
    }

    public void addDiva_dimension(Diva_dimension diva_dimension) {
        this.diva_dimensions.add(diva_dimension);
    }
    public List<diva_Property> getDiva_propertys() {
        return diva_propertys;
    }

    public void addDiva_property(Diva_property diva_property) {
        this.diva_propertys.add(diva_property);
    }
    public List<diva_Variable> getDiva_variables() {
        return diva_variables;
    }

    public void addDiva_variable(Diva_variable diva_variable) {
        this.diva_variables.add(diva_variable);
    }

}