





import java.util.List;
import java.util.ArrayList;

public class ptnetLoLA_Node  {

    private String name;
    private String type;



    public ptnetLoLA_Node(
        String name,        String type    ) {
        this.name = name;
        this.type = type;
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