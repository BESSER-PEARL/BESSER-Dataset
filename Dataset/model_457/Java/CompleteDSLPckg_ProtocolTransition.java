





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ProtocolTransition extends Transition {






    private CompleteDSLPckg_Constraint completedslpckg_constraint;




    private List<CompleteDSLPckg_Operation> completedslpckg_operations;




    private CompleteDSLPckg_Constraint completedslpckg_constraint;


    public CompleteDSLPckg_ProtocolTransition(
    ) {
        super(
        );
        this.completedslpckg_operations = new ArrayList<>();
    }

    public CompleteDSLPckg_ProtocolTransition(
        ArrayList<CompleteDSLPckg_Operation> completedslpckg_operations    ) {
        this.completedslpckg_operations = completedslpckg_operations;
    }


    public CompleteDSLPckg_Constraint getCompletedslpckg_constraint() {
        return completedslpckg_constraint;
    }

    public void setCompletedslpckg_constraint(CompleteDSLPckg_Constraint completedslpckg_constraint) {
        this.completedslpckg_constraint = completedslpckg_constraint;
    }
    public List<CompleteDSLPckg_Operation> getCompletedslpckg_operations() {
        return completedslpckg_operations;
    }

    public void addCompletedslpckg_operation(Completedslpckg_operation completedslpckg_operation) {
        this.completedslpckg_operations.add(completedslpckg_operation);
    }
    public CompleteDSLPckg_Constraint getCompletedslpckg_constraint() {
        return completedslpckg_constraint;
    }

    public void setCompletedslpckg_constraint(CompleteDSLPckg_Constraint completedslpckg_constraint) {
        this.completedslpckg_constraint = completedslpckg_constraint;
    }

}