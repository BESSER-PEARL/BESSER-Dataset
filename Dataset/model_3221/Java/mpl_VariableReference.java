





import java.util.List;
import java.util.ArrayList;

public class mpl_VariableReference extends AtomicExpression {






    private mpl_Assignment mpl_assignment;




    private mpl_Trace mpl_trace;


    public mpl_VariableReference(
    ) {
        super(
        );
    }



    public mpl_Assignment getMpl_assignment() {
        return mpl_assignment;
    }

    public void setMpl_assignment(mpl_Assignment mpl_assignment) {
        this.mpl_assignment = mpl_assignment;
    }
    public mpl_Trace getMpl_trace() {
        return mpl_trace;
    }

    public void setMpl_trace(mpl_Trace mpl_trace) {
        this.mpl_trace = mpl_trace;
    }

}