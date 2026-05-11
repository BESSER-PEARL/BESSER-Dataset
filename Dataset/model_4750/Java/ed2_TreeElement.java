





import java.util.List;
import java.util.ArrayList;

public class ed2_TreeElement  {

    private String index;
    private String name;
    private String type;



    public ed2_TreeElement(
        String index,        String name,        String type    ) {
        this.index = index;
        this.name = name;
        this.type = type;
    }


    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
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