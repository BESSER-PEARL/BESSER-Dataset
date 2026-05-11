





import java.util.List;
import java.util.ArrayList;

public class model_partnerlinktype_Role extends ExtensibilityElement {

    private String ID;
    private String name;
    private String portType;



    public model_partnerlinktype_Role(
        String ID,        String name,        String portType    ) {
        super(
        );
        this.ID = ID;
        this.name = name;
        this.portType = portType;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPorttype() {
        return portType;
    }

    public void setPorttype(String portType) {
        this.portType = portType;
    }


}