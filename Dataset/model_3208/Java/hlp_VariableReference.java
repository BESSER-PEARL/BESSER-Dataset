





import java.util.List;
import java.util.ArrayList;

public class hlp_VariableReference extends AtomicExpression {






    private hlp_SynchronizedStatement hlp_synchronizedstatement;




    private hlp_Variable hlp_variable;




    private hlp_ForLoop hlp_forloop;




    private hlp_Assignment hlp_assignment;


    public hlp_VariableReference(
    ) {
        super(
        );
    }



    public hlp_SynchronizedStatement getHlp_synchronizedstatement() {
        return hlp_synchronizedstatement;
    }

    public void setHlp_synchronizedstatement(hlp_SynchronizedStatement hlp_synchronizedstatement) {
        this.hlp_synchronizedstatement = hlp_synchronizedstatement;
    }
    public hlp_Variable getHlp_variable() {
        return hlp_variable;
    }

    public void setHlp_variable(hlp_Variable hlp_variable) {
        this.hlp_variable = hlp_variable;
    }
    public hlp_ForLoop getHlp_forloop() {
        return hlp_forloop;
    }

    public void setHlp_forloop(hlp_ForLoop hlp_forloop) {
        this.hlp_forloop = hlp_forloop;
    }
    public hlp_Assignment getHlp_assignment() {
        return hlp_assignment;
    }

    public void setHlp_assignment(hlp_Assignment hlp_assignment) {
        this.hlp_assignment = hlp_assignment;
    }

}