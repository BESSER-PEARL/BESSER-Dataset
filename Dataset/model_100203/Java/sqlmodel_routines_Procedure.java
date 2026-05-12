





import java.util.List;
import java.util.ArrayList;

public class sqlmodel_routines_Procedure extends Routine {

    private int maxResultSets;
    private boolean oldSavePoint;



    public sqlmodel_routines_Procedure(
        int maxResultSets,        boolean oldSavePoint    ) {
        super(
        );
        this.maxResultSets = maxResultSets;
        this.oldSavePoint = oldSavePoint;
    }


    public int getMaxresultsets() {
        return maxResultSets;
    }

    public void setMaxresultsets(int maxResultSets) {
        this.maxResultSets = maxResultSets;
    }
    public boolean getOldsavepoint() {
        return oldSavePoint;
    }

    public void setOldsavepoint(boolean oldSavePoint) {
        this.oldSavePoint = oldSavePoint;
    }


}