





import java.util.List;
import java.util.ArrayList;

public class qvtoperational_cst_AssignStatementCS extends StatementCS {

    private boolean incremental;



    public qvtoperational_cst_AssignStatementCS(
        boolean incremental    ) {
        super(
        );
        this.incremental = incremental;
    }


    public boolean getIncremental() {
        return incremental;
    }

    public void setIncremental(boolean incremental) {
        this.incremental = incremental;
    }


}