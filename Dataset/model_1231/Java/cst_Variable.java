





import java.util.List;
import java.util.ArrayList;

public class cst_Variable extends CSTNode {

    private String name;
    private String type;



    public cst_Variable(
        String name,        String type    ) {
        super(
        );
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