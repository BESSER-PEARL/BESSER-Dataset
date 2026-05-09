





import java.util.List;
import java.util.ArrayList;

public class gbind_simpleocl_StaticNavigationOrAttributeCall extends StaticPropertyCall {

    private String name;



    public gbind_simpleocl_StaticNavigationOrAttributeCall(
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