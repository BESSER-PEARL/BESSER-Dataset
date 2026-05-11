





import java.util.List;
import java.util.ArrayList;

public class mtm_di_DiagramElement  {

    private String anyAttribute;
    private String id;



    public mtm_di_DiagramElement(
        String anyAttribute,        String id    ) {
        this.anyAttribute = anyAttribute;
        this.id = id;
    }


    public String getAnyattribute() {
        return anyAttribute;
    }

    public void setAnyattribute(String anyAttribute) {
        this.anyAttribute = anyAttribute;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}