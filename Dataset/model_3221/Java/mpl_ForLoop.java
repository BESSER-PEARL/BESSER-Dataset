





import java.util.List;
import java.util.ArrayList;

public class mpl_ForLoop extends Statement {

    private String direction;





    private mpl_Assignment mpl_assignment;




    private mpl_Expression mpl_expression;


    public mpl_ForLoop(
        String direction    ) {
        super(
        );
        this.direction = direction;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
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