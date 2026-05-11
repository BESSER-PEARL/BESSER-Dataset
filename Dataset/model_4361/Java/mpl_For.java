





import java.util.List;
import java.util.ArrayList;

public class mpl_For extends Loop {

    private String downwards;





    private mpl_Expression mpl_expression;




    private mpl_Assignment mpl_assignment;


    public mpl_For(
        String downwards    ) {
        super(
        );
        this.downwards = downwards;
    }


    public String getDownwards() {
        return downwards;
    }

    public void setDownwards(String downwards) {
        this.downwards = downwards;
    }

    public mpl_Expression getMpl_expression() {
        return mpl_expression;
    }

    public void setMpl_expression(mpl_Expression mpl_expression) {
        this.mpl_expression = mpl_expression;
    }
    public mpl_Assignment getMpl_assignment() {
        return mpl_assignment;
    }

    public void setMpl_assignment(mpl_Assignment mpl_assignment) {
        this.mpl_assignment = mpl_assignment;
    }

}