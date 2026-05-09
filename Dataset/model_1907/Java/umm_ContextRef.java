





import java.util.List;
import java.util.ArrayList;

public class umm_ContextRef  {

    private String name;





    private umm_Constraint umm_constraint;


    public umm_ContextRef(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public umm_Constraint getUmm_constraint() {
        return umm_constraint;
    }

    public void setUmm_constraint(umm_Constraint umm_constraint) {
        this.umm_constraint = umm_constraint;
    }

}