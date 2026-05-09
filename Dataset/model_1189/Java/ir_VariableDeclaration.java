





import java.util.List;
import java.util.ArrayList;

public class ir_VariableDeclaration  {

    private String name;





    private ir_TypeRef ir_typeref;


    public ir_VariableDeclaration(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ir_TypeRef getIr_typeref() {
        return ir_typeref;
    }

    public void setIr_typeref(ir_TypeRef ir_typeref) {
        this.ir_typeref = ir_typeref;
    }

}