





import java.util.List;
import java.util.ArrayList;

public class datatype_ConstraintRule  {






    private datatype_Property datatype_property;




    private List<datatype_Constraint> datatype_constraints;


    public datatype_ConstraintRule(
    ) {
        this.datatype_constraints = new ArrayList<>();
    }

    public datatype_ConstraintRule(
        ArrayList<datatype_Constraint> datatype_constraints    ) {
        this.datatype_constraints = datatype_constraints;
    }


    public datatype_Property getDatatype_property() {
        return datatype_property;
    }

    public void setDatatype_property(datatype_Property datatype_property) {
        this.datatype_property = datatype_property;
    }
    public List<datatype_Constraint> getDatatype_constraints() {
        return datatype_constraints;
    }

    public void addDatatype_constraint(Datatype_constraint datatype_constraint) {
        this.datatype_constraints.add(datatype_constraint);
    }

}