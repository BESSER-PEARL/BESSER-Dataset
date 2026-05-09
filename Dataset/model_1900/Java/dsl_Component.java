





import java.util.List;
import java.util.ArrayList;

public class dsl_Component  {

    private String name;





    private dsl_Architecture dsl_architecture;


    public dsl_Component(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Architecture getDsl_architecture() {
        return dsl_architecture;
    }

    public void setDsl_architecture(dsl_Architecture dsl_architecture) {
        this.dsl_architecture = dsl_architecture;
    }

}