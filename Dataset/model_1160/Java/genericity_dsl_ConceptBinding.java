





import java.util.List;
import java.util.ArrayList;

public class genericity_dsl_ConceptBinding extends LocatedElement {

    private String debugName;



    public genericity_dsl_ConceptBinding(
        String debugName    ) {
        super(
        );
        this.debugName = debugName;
    }


    public String getDebugname() {
        return debugName;
    }

    public void setDebugname(String debugName) {
        this.debugName = debugName;
    }


}