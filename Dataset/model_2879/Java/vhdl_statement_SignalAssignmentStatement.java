





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_SignalAssignmentStatement extends Statement {

    private boolean postponed;
    private boolean guarded;



    public vhdl_statement_SignalAssignmentStatement(
        boolean postponed,        boolean guarded    ) {
        super(
        );
        this.postponed = postponed;
        this.guarded = guarded;
    }


    public boolean getPostponed() {
        return postponed;
    }

    public void setPostponed(boolean postponed) {
        this.postponed = postponed;
    }
    public boolean getGuarded() {
        return guarded;
    }

    public void setGuarded(boolean guarded) {
        this.guarded = guarded;
    }


}