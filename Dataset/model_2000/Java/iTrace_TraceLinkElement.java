





import java.util.List;
import java.util.ArrayList;

public class iTrace_TraceLinkElement  {

    private String ref;
    private String name;
    private String type;



    public iTrace_TraceLinkElement(
        String ref,        String name,        String type    ) {
        this.ref = ref;
        this.name = name;
        this.type = type;
    }


    public String getRef() {
        return ref;
    }

    public void setRef(String ref) {
        this.ref = ref;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}