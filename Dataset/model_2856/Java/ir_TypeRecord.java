





import java.util.List;
import java.util.ArrayList;

public class ir_TypeRecord extends Node, Type {






    private List<ir_Variable> ir_variables;


    public ir_TypeRecord(
    ) {
        super(
        );
        this.ir_variables = new ArrayList<>();
    }

    public ir_TypeRecord(
        ArrayList<ir_Variable> ir_variables    ) {
        this.ir_variables = ir_variables;
    }


    public List<ir_Variable> getIr_variables() {
        return ir_variables;
    }

    public void addIr_variable(Ir_variable ir_variable) {
        this.ir_variables.add(ir_variable);
    }

}