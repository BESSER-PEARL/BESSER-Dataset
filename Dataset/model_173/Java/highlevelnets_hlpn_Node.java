





import java.util.List;
import java.util.ArrayList;

public class highlevelnets_hlpn_Node extends INetElement {

    private int secondTimeConstraint;
    private int firstTimeConstraint;



    public highlevelnets_hlpn_Node(
        int secondTimeConstraint,        int firstTimeConstraint    ) {
        super(
        );
        this.secondTimeConstraint = secondTimeConstraint;
        this.firstTimeConstraint = firstTimeConstraint;
    }


    public int getSecondtimeconstraint() {
        return secondTimeConstraint;
    }

    public void setSecondtimeconstraint(int secondTimeConstraint) {
        this.secondTimeConstraint = secondTimeConstraint;
    }
    public int getFirsttimeconstraint() {
        return firstTimeConstraint;
    }

    public void setFirsttimeconstraint(int firstTimeConstraint) {
        this.firstTimeConstraint = firstTimeConstraint;
    }


}