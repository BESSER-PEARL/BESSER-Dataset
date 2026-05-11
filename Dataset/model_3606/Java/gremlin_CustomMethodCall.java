





import java.util.List;
import java.util.ArrayList;

public class gremlin_CustomMethodCall extends MethodCall {

    private String name;



    public gremlin_CustomMethodCall(
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