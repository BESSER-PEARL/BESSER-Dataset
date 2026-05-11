





import java.util.List;
import java.util.ArrayList;

public class ed2_TreeObject  {

    private String index;
    private String type;
    private String name;



    public ed2_TreeObject(
        String index,        String type,        String name    ) {
        this.index = index;
        this.type = type;
        this.name = name;
    }


    public String getIndex() {
        return index;
    }

    public void setIndex(String index) {
        this.index = index;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}