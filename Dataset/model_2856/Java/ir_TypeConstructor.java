





import java.util.List;
import java.util.ArrayList;

public class ir_TypeConstructor extends Declaration {






    private ir_TypeDeclaration ir_typedeclaration;




    private ir_TypeDeclaration ir_typedeclaration;




    private List<ir_Variable> ir_variables;


    public ir_TypeConstructor(
    ) {
        super(
        );
        this.ir_variables = new ArrayList<>();
    }

    public ir_TypeConstructor(
        ArrayList<ir_Variable> ir_variables    ) {
        this.ir_variables = ir_variables;
    }


    public ir_TypeDeclaration getIr_typedeclaration() {
        return ir_typedeclaration;
    }

    public void setIr_typedeclaration(ir_TypeDeclaration ir_typedeclaration) {
        this.ir_typedeclaration = ir_typedeclaration;
    }
    public ir_TypeDeclaration getIr_typedeclaration() {
        return ir_typedeclaration;
    }

    public void setIr_typedeclaration(ir_TypeDeclaration ir_typedeclaration) {
        this.ir_typedeclaration = ir_typedeclaration;
    }
    public List<ir_Variable> getIr_variables() {
        return ir_variables;
    }

    public void addIr_variable(Ir_variable ir_variable) {
        this.ir_variables.add(ir_variable);
    }

}