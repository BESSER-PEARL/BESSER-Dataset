





import java.util.List;
import java.util.ArrayList;

public class xmof_CompleteStructuredActivities_StructuredActivityNode extends Action {

    private boolean mustIsolate;



    public xmof_CompleteStructuredActivities_StructuredActivityNode(
        boolean mustIsolate    ) {
        super(
        );
        this.mustIsolate = mustIsolate;
    }


    public boolean getMustisolate() {
        return mustIsolate;
    }

    public void setMustisolate(boolean mustIsolate) {
        this.mustIsolate = mustIsolate;
    }


}