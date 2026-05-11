





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_ProcedureCallStatement extends Statement {

    private boolean postponed;



    public vhdl_statement_ProcedureCallStatement(
        boolean postponed    ) {
        super(
        );
        this.postponed = postponed;
    }


    public boolean getPostponed() {
        return postponed;
    }

    public void setPostponed(boolean postponed) {
        this.postponed = postponed;
    }


}