





import java.util.List;
import java.util.ArrayList;

public class UML_Activity_mine_Element  {

    private String properties;
    private String name;
    private String elementID;



    public UML_Activity_mine_Element(
        String properties,        String name,        String elementID    ) {
        this.properties = properties;
        this.name = name;
        this.elementID = elementID;
    }


    public String getProperties() {
        return properties;
    }

    public void setProperties(String properties) {
        this.properties = properties;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getElementid() {
        return elementID;
    }

    public void setElementid(String elementID) {
        this.elementID = elementID;
    }


}