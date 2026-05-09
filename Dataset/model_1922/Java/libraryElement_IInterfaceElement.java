





import java.util.List;
import java.util.ArrayList;

public class libraryElement_IInterfaceElement extends INamedElement {

    private String isInput;
    private String typeName;



    public libraryElement_IInterfaceElement(
        String isInput,        String typeName    ) {
        super(
        );
        this.isInput = isInput;
        this.typeName = typeName;
    }


    public String getIsinput() {
        return isInput;
    }

    public void setIsinput(String isInput) {
        this.isInput = isInput;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }


}