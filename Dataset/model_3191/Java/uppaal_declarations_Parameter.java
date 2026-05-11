





import java.util.List;
import java.util.ArrayList;

public class uppaal_declarations_Parameter  {

    private String callType;





    private VariableDeclaration variabledeclaration;


    public uppaal_declarations_Parameter(
        String callType    ) {
        this.callType = callType;
    }


    public String getCalltype() {
        return callType;
    }

    public void setCalltype(String callType) {
        this.callType = callType;
    }

    public VariableDeclaration getVariabledeclaration() {
        return variabledeclaration;
    }

    public void setVariabledeclaration(VariableDeclaration variabledeclaration) {
        this.variabledeclaration = variabledeclaration;
    }

}