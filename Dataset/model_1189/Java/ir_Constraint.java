





import java.util.List;
import java.util.ArrayList;

public class ir_Constraint  {

    private String name;





    private ir_Specification ir_specification;


    public ir_Constraint(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ir_Specification getIr_specification() {
        return ir_specification;
    }

    public void setIr_specification(ir_Specification ir_specification) {
        this.ir_specification = ir_specification;
    }

}