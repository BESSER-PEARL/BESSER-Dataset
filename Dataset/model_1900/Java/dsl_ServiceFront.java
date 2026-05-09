





import java.util.List;
import java.util.ArrayList;

public class dsl_ServiceFront extends AbstractFrontElement {

    private String method;
    private String name;



    public dsl_ServiceFront(
        String method,        String name    ) {
        super(
        );
        this.method = method;
        this.name = name;
    }


    public String getMethod() {
        return method;
    }

    public void setMethod(String method) {
        this.method = method;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}