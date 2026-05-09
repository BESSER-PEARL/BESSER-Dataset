





import java.util.List;
import java.util.ArrayList;

public class webapp_Action  {

    private String name;
    private String returnType;



    public webapp_Action(
        String name,        String returnType    ) {
        this.name = name;
        this.returnType = returnType;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }


}