





import java.util.List;
import java.util.ArrayList;

public class vhdl_statement_ProcessStatement extends Statement {

    private boolean postponed;



    public vhdl_statement_ProcessStatement(
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