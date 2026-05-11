





import java.util.List;
import java.util.ArrayList;

public class datatype_Constraint  {

    private String type;
    private String constraintValues;





    private datatype_ConstraintRule datatype_constraintrule;


    public datatype_Constraint(
        String type,        String constraintValues    ) {
        this.type = type;
        this.constraintValues = constraintValues;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getConstraintvalues() {
        return constraintValues;
    }

    public void setConstraintvalues(String constraintValues) {
        this.constraintValues = constraintValues;
    }

    public datatype_ConstraintRule getDatatype_constraintrule() {
        return datatype_constraintrule;
    }

    public void setDatatype_constraintrule(datatype_ConstraintRule datatype_constraintrule) {
        this.datatype_constraintrule = datatype_constraintrule;
    }

}