





import java.util.List;
import java.util.ArrayList;

public class dsl_Container extends AbstractFrontElement {

    private String name;





    private dsl_Functionality dsl_functionality;


    public dsl_Container(
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

    public dsl_Functionality getDsl_functionality() {
        return dsl_functionality;
    }

    public void setDsl_functionality(dsl_Functionality dsl_functionality) {
        this.dsl_functionality = dsl_functionality;
    }

}