





import java.util.List;
import java.util.ArrayList;

public class vcml_ConstraintObject  {

    private String name;





    private vcml_ConstraintSource vcml_constraintsource;


    public vcml_ConstraintObject(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public vcml_ConstraintSource getVcml_constraintsource() {
        return vcml_constraintsource;
    }

    public void setVcml_constraintsource(vcml_ConstraintSource vcml_constraintsource) {
        this.vcml_constraintsource = vcml_constraintsource;
    }

}