





import java.util.List;
import java.util.ArrayList;

public class imperativeoclcs_AssignStatementCS extends StatementCS {

    private boolean incremental;



    public imperativeoclcs_AssignStatementCS(
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