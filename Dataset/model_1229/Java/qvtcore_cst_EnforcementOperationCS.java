





import java.util.List;
import java.util.ArrayList;

public class qvtcore_cst_EnforcementOperationCS extends CSTNode {

    private boolean deletion;



    public qvtcore_cst_EnforcementOperationCS(
        boolean deletion    ) {
        super(
        );
        this.deletion = deletion;
    }


    public boolean getDeletion() {
        return deletion;
    }

    public void setDeletion(boolean deletion) {
        this.deletion = deletion;
    }


}