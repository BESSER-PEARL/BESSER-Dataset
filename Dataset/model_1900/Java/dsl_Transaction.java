





import java.util.List;
import java.util.ArrayList;

public class dsl_Transaction  {

    private String type;





    private dsl_SpecialEntity dsl_specialentity;


    public dsl_Transaction(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public dsl_SpecialEntity getDsl_specialentity() {
        return dsl_specialentity;
    }

    public void setDsl_specialentity(dsl_SpecialEntity dsl_specialentity) {
        this.dsl_specialentity = dsl_specialentity;
    }

}