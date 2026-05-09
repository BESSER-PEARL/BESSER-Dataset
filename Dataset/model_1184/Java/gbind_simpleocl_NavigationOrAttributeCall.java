





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_NavigationOrAttributeCall extends PropertyCall {

    private String name;



    public gbind_simpleocl_NavigationOrAttributeCall(
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