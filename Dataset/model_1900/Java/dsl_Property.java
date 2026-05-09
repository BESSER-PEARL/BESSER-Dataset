





import java.util.List;
import java.util.ArrayList;

public class dsl_Property  {

    private String name;





    private dsl_Type dsl_type;




    private dsl_GeneralEntity dsl_generalentity;


    public dsl_Property(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public dsl_Type getDsl_type() {
        return dsl_type;
    }

    public void setDsl_type(dsl_Type dsl_type) {
        this.dsl_type = dsl_type;
    }
    public dsl_GeneralEntity getDsl_generalentity() {
        return dsl_generalentity;
    }

    public void setDsl_generalentity(dsl_GeneralEntity dsl_generalentity) {
        this.dsl_generalentity = dsl_generalentity;
    }

}