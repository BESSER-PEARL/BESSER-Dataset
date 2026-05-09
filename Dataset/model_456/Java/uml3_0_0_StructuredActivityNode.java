





import java.util.List;
import java.util.ArrayList;

public class uml3_0_0_StructuredActivityNode extends Namespace, ActivityGroup, Action {

    private String mustIsolate;



    public uml3_0_0_StructuredActivityNode(
        String mustIsolate    ) {
        super(
        );
        this.mustIsolate = mustIsolate;
    }


    public String getMustisolate() {
        return mustIsolate;
    }

    public void setMustisolate(String mustIsolate) {
        this.mustIsolate = mustIsolate;
    }


}