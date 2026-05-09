





import java.util.List;
import java.util.ArrayList;

public class uml_StructuredActivityNode extends Namespace, ActivityGroup, Action {

    private String mustIsolate;



    public uml_StructuredActivityNode(
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