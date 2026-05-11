





import java.util.List;
import java.util.ArrayList;

public class C_Declarations_PrototypeFunctionDeclaration extends Declaration {

    private String functionModifier;
    private String isAPointer;





    private Types_Type types_type;


    public C_Declarations_PrototypeFunctionDeclaration(
        String functionModifier,        String isAPointer    ) {
        super(
        );
        this.functionModifier = functionModifier;
        this.isAPointer = isAPointer;
    }


    public String getFunctionmodifier() {
        return functionModifier;
    }

    public void setFunctionmodifier(String functionModifier) {
        this.functionModifier = functionModifier;
    }
    public String getIsapointer() {
        return isAPointer;
    }

    public void setIsapointer(String isAPointer) {
        this.isAPointer = isAPointer;
    }

    public Types_Type getTypes_type() {
        return types_type;
    }

    public void setTypes_type(Types_Type types_type) {
        this.types_type = types_type;
    }

}