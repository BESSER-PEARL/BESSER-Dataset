





import java.util.List;
import java.util.ArrayList;

public class Janus_essentialocl_Variable extends TypedElement {

    private String varType;





    private Parameter parameter;


    public Janus_essentialocl_Variable(
        String varType    ) {
        super(
        );
        this.varType = varType;
    }


    public String getVartype() {
        return varType;
    }

    public void setVartype(String varType) {
        this.varType = varType;
    }

    public Parameter getParameter() {
        return parameter;
    }

    public void setParameter(Parameter parameter) {
        this.parameter = parameter;
    }

}