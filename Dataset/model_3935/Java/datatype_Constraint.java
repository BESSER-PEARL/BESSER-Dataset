





import java.util.List;
import java.util.ArrayList;

public class datatype_Constraint  {

    private String constraintValues;
    private String type;



    public datatype_Constraint(
        String constraintValues,        String type    ) {
        this.constraintValues = constraintValues;
        this.type = type;
    }


    public String getConstraintvalues() {
        return constraintValues;
    }

    public void setConstraintvalues(String constraintValues) {
        this.constraintValues = constraintValues;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}