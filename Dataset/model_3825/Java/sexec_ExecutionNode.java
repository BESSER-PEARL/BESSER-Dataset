





import java.util.List;
import java.util.ArrayList;

public class sexec_ExecutionNode extends NamedElement, MappedElement {

    private String simpleName;



    public sexec_ExecutionNode(
        String simpleName    ) {
        super(
        );
        this.simpleName = simpleName;
    }


    public String getSimplename() {
        return simpleName;
    }

    public void setSimplename(String simpleName) {
        this.simpleName = simpleName;
    }


}