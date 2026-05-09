





import java.util.List;
import java.util.ArrayList;

public class ocl_dm_EAttribute  {

    private String type;
    private String name;



    public ocl_dm_EAttribute(
        String type,        String name    ) {
        this.type = type;
        this.name = name;
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