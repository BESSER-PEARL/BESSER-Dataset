





import java.util.List;
import java.util.ArrayList;

public class UML2WithID_StructuredActivityNode extends Namespace, Action, ActivityGroup {

    private boolean mustIsolate;



    public UML2WithID_StructuredActivityNode(
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