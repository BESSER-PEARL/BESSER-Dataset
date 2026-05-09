





import java.util.List;
import java.util.ArrayList;

public class ACG_Node extends StatementBlock, ACGElement {

    private String element;
    private String mode;



    public ACG_Node(
        String element,        String mode    ) {
        super(
        );
        this.element = element;
        this.mode = mode;
    }


    public String getElement() {
        return element;
    }

    public void setElement(String element) {
        this.element = element;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }


}