





import java.util.List;
import java.util.ArrayList;

public class ir_BaseType extends IrType {

    private String primitive;





    private List<ir_Expression> ir_expressions;




    private ir_Arg ir_arg;




    private ir_Function ir_function;




    private ir_SimpleVariable ir_simplevariable;


    public ir_BaseType(
        String primitive    ) {
        super(
        );
        this.primitive = primitive;
        this.ir_expressions = new ArrayList<>();
    }

    public ir_BaseType(
        String primitive        ArrayList<ir_Expression> ir_expressions    ) {
        this.primitive = primitive;
        this.ir_expressions = ir_expressions;
    }

    public String getPrimitive() {
        return primitive;
    }

    public void setPrimitive(String primitive) {
        this.primitive = primitive;
    }

    public List<ir_Expression> getIr_expressions() {
        return ir_expressions;
    }

    public void addIr_expression(Ir_expression ir_expression) {
        this.ir_expressions.add(ir_expression);
    }
    public ir_Arg getIr_arg() {
        return ir_arg;
    }

    public void setIr_arg(ir_Arg ir_arg) {
        this.ir_arg = ir_arg;
    }
    public ir_Function getIr_function() {
        return ir_function;
    }

    public void setIr_function(ir_Function ir_function) {
        this.ir_function = ir_function;
    }
    public ir_SimpleVariable getIr_simplevariable() {
        return ir_simplevariable;
    }

    public void setIr_simplevariable(ir_SimpleVariable ir_simplevariable) {
        this.ir_simplevariable = ir_simplevariable;
    }

}