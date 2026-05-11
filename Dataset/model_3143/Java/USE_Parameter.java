





import java.util.List;
import java.util.ArrayList;

public class USE_Parameter  {

    private String name;





    private USE_Type use_type;


    public USE_Parameter(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public USE_Type getUse_type() {
        return use_type;
    }

    public void setUse_type(USE_Type use_type) {
        this.use_type = use_type;
    }

}