





import java.util.List;
import java.util.ArrayList;

public class spinefm_UserActionModel_UserRenameElement extends UserAction {

    private String elementType;
    private String elementID;
    private String name;



    public spinefm_UserActionModel_UserRenameElement(
        String elementType,        String elementID,        String name    ) {
        super(
        );
        this.elementType = elementType;
        this.elementID = elementID;
        this.name = name;
    }


    public String getElementtype() {
        return elementType;
    }

    public void setElementtype(String elementType) {
        this.elementType = elementType;
    }
    public String getElementid() {
        return elementID;
    }

    public void setElementid(String elementID) {
        this.elementID = elementID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}