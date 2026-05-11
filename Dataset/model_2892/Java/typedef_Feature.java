





import java.util.List;
import java.util.ArrayList;

public class typedef_Feature  {

    private String name;





    private typedef_Type typedef_type;


    public typedef_Feature(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public typedef_Type getTypedef_type() {
        return typedef_type;
    }

    public void setTypedef_type(typedef_Type typedef_type) {
        this.typedef_type = typedef_type;
    }

}