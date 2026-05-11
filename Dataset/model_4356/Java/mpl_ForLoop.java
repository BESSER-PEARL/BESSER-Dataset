





import java.util.List;
import java.util.ArrayList;

public class mpl_ForLoop extends Statement {

    private boolean increment;





    private mpl_Assignment mpl_assignment;




    private mpl_Expression mpl_expression;


    public mpl_ForLoop(
        boolean increment    ) {
        super(
        );
        this.increment = increment;
    }


    public boolean getIncrement() {
        return increment;
    }

    public void setIncrement(boolean increment) {
        this.increment = increment;
    }

    public mpl_Assignment getMpl_assignment() {
        return mpl_assignment;
    }

    public void setMpl_assignment(mpl_Assignment mpl_assignment) {
        this.mpl_assignment = mpl_assignment;
    }
    public mpl_Expression getMpl_expression() {
        return mpl_expression;
    }

    public void setMpl_expression(mpl_Expression mpl_expression) {
        this.mpl_expression = mpl_expression;
    }

}