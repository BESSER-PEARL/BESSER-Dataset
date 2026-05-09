





import java.util.List;
import java.util.ArrayList;

public class dsl_AbstractMethod  {

    private String name;





    private dsl_AbstractClass dsl_abstractclass;


    public dsl_AbstractMethod(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_AbstractClass getDsl_abstractclass() {
        return dsl_abstractclass;
    }

    public void setDsl_abstractclass(dsl_AbstractClass dsl_abstractclass) {
        this.dsl_abstractclass = dsl_abstractclass;
    }

}