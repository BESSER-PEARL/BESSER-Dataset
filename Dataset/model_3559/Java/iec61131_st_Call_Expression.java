





import java.util.List;
import java.util.ArrayList;

public class iec61131_st_Call_Expression extends Primary_Expression {






    private List<Param_Assignment> param_assignments;


    public iec61131_st_Call_Expression(
    ) {
        super(
        );
        this.param_assignments = new ArrayList<>();
    }

    public iec61131_st_Call_Expression(
        ArrayList<Param_Assignment> param_assignments    ) {
        this.param_assignments = param_assignments;
    }


    public List<Param_Assignment> getParam_assignments() {
        return param_assignments;
    }

    public void addParam_assignment(Param_assignment param_assignment) {
        this.param_assignments.add(param_assignment);
    }

}