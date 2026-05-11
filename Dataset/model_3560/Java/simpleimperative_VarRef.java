





import java.util.List;
import java.util.ArrayList;

public class simpleimperative_VarRef extends Expression {

    private String varRef;



    public simpleimperative_VarRef(
        String varRef    ) {
        super(
        );
        this.varRef = varRef;
    }


    public String getVarref() {
        return varRef;
    }

    public void setVarref(String varRef) {
        this.varRef = varRef;
    }


}