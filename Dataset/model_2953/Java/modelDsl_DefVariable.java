





import java.util.List;
import java.util.ArrayList;

public class modelDsl_DefVariable  {

    private String name;





    private modelDsl_Method modeldsl_method;


    public modelDsl_DefVariable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public modelDsl_Method getModeldsl_method() {
        return modeldsl_method;
    }

    public void setModeldsl_method(modelDsl_Method modeldsl_method) {
        this.modeldsl_method = modeldsl_method;
    }

}