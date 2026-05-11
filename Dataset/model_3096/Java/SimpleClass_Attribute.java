





import java.util.List;
import java.util.ArrayList;

public class SimpleClass_Attribute  {

    private String is_primary;
    private String name;



    public SimpleClass_Attribute(
        String is_primary,        String name    ) {
        this.is_primary = is_primary;
        this.name = name;
    }


    public String getIs_primary() {
        return is_primary;
    }

    public void setIs_primary(String is_primary) {
        this.is_primary = is_primary;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}