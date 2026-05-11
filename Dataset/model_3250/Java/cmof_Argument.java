





import java.util.List;
import java.util.ArrayList;

public class cmof_Argument  {

    private String name;





    private cmof_Object cmof_object;


    public cmof_Argument(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public cmof_Object getCmof_object() {
        return cmof_object;
    }

    public void setCmof_object(cmof_Object cmof_object) {
        this.cmof_object = cmof_object;
    }

}