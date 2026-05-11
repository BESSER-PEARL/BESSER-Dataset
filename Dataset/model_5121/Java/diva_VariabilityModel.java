





import java.util.List;
import java.util.ArrayList;

public class diva_VariabilityModel extends DiVAModelElement {






    private List<diva_Constraint> diva_constraints;




    private List<diva_Variable> diva_variables;




    private List<diva_Property> diva_propertys;




    private List<diva_Dimension> diva_dimensions;




    private diva_BaseModel diva_basemodel;




    private List<diva_Rule> diva_rules;


    public diva_VariabilityModel(
    ) {
        super(
        );
        this.diva_constraints = new ArrayList<>();
        this.diva_variables = new ArrayList<>();
        this.diva_propertys = new ArrayList<>();
        this.diva_dimensions = new ArrayList<>();
        this.diva_rules = new ArrayList<>();
    }

    public diva_VariabilityModel(
        ArrayList<diva_Constraint> diva_constraints,        ArrayList<diva_Variable> diva_variables,        ArrayList<diva_Property> diva_propertys,        ArrayList<diva_Dimension> diva_dimensions,        ArrayList<diva_Rule> diva_rules    ) {
        this.diva_constraints = diva_constraints;
        this.diva_variables = diva_variables;
        this.diva_propertys = diva_propertys;
        this.diva_dimensions = diva_dimensions;
        this.diva_rules = diva_rules;
    }


    public List<diva_Constraint> getDiva_constraints() {
        return diva_constraints;
    }

    public void addDiva_constraint(Diva_constraint diva_constraint) {
        this.diva_constraints.add(diva_constraint);
    }
    public List<diva_Variable> getDiva_variables() {
        return diva_variables;
    }

    public void addDiva_variable(Diva_variable diva_variable) {
        this.diva_variables.add(diva_variable);
    }
    public List<diva_Property> getDiva_propertys() {
        return diva_propertys;
    }

    public void addDiva_property(Diva_property diva_property) {
        this.diva_propertys.add(diva_property);
    }
    public List<diva_Dimension> getDiva_dimensions() {
        return diva_dimensions;
    }

    public void addDiva_dimension(Diva_dimension diva_dimension) {
        this.diva_dimensions.add(diva_dimension);
    }
    public diva_BaseModel getDiva_basemodel() {
        return diva_basemodel;
    }

    public void setDiva_basemodel(diva_BaseModel diva_basemodel) {
        this.diva_basemodel = diva_basemodel;
    }
    public List<diva_Rule> getDiva_rules() {
        return diva_rules;
    }

    public void addDiva_rule(Diva_rule diva_rule) {
        this.diva_rules.add(diva_rule);
    }

}