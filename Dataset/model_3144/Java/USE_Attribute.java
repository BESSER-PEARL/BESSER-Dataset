





import java.util.List;
import java.util.ArrayList;

public class USE_Attribute  {

    private String name;





    private USE_Class use_class;


    public USE_Attribute(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public USE_Class getUse_class() {
        return use_class;
    }

    public void setUse_class(USE_Class use_class) {
        this.use_class = use_class;
    }

}