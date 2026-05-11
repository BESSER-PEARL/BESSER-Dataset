





import java.util.List;
import java.util.ArrayList;

public class ir_Annotation  {

    private String name;





    private ir_Node ir_node;


    public ir_Annotation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ir_Node getIr_node() {
        return ir_node;
    }

    public void setIr_node(ir_Node ir_node) {
        this.ir_node = ir_node;
    }

}