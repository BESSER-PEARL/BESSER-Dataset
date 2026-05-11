





import java.util.List;
import java.util.ArrayList;

public class go_DecFunc extends Greeting {

    private String returnType;
    private String name;



    public go_DecFunc(
        String returnType,        String name    ) {
        super(
        );
        this.returnType = returnType;
        this.name = name;
    }


    public String getReturntype() {
        return returnType;
    }

    public void setReturntype(String returnType) {
        this.returnType = returnType;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}