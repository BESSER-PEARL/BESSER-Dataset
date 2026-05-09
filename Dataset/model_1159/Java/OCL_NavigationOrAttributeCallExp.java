





import java.util.List;
import java.util.ArrayList;

public class OCL_NavigationOrAttributeCallExp extends PropertyCallExp {

    private String name;



    public OCL_NavigationOrAttributeCallExp(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}