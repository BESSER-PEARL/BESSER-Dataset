





import java.util.List;
import java.util.ArrayList;

public class ACG_Node extends StatementBlock, ACGElement {

    private String mode;
    private String element;



    public ACG_Node(
        String mode,        String element    ) {
        super(
        );
        this.mode = mode;
        this.element = element;
    }


    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public String getElement() {
        return element;
    }

    public void setElement(String element) {
        this.element = element;
    }


}