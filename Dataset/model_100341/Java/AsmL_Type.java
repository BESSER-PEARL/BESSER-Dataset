





import java.util.List;
import java.util.ArrayList;

public class AsmL_Type extends AsmLElement {

    private String withNull;





    private Method method;




    private Parameter parameter;


    public AsmL_Type(
        String withNull    ) {
        super(
        );
        this.withNull = withNull;
    }


    public String getWithnull() {
        return withNull;
    }

    public void setWithnull(String withNull) {
        this.withNull = withNull;
    }

    public Method getMethod() {
        return method;
    }

    public void setMethod(Method method) {
        this.method = method;
    }
    public Parameter getParameter() {
        return parameter;
    }

    public void setParameter(Parameter parameter) {
        this.parameter = parameter;
    }

}