





import java.util.List;
import java.util.ArrayList;

public class ryz_ActionMethod extends NamedElement {

    private String httpMethod;
    private String returns;





    private List<ryz_Parameter> ryz_parameters;


    public ryz_ActionMethod(
        String httpMethod,        String returns    ) {
        super(
        );
        this.httpMethod = httpMethod;
        this.returns = returns;
        this.ryz_parameters = new ArrayList<>();
    }

    public ryz_ActionMethod(
        String httpMethod,        String returns        ArrayList<ryz_Parameter> ryz_parameters    ) {
        this.httpMethod = httpMethod;
        this.returns = returns;
        this.ryz_parameters = ryz_parameters;
    }

    public String getHttpmethod() {
        return httpMethod;
    }

    public void setHttpmethod(String httpMethod) {
        this.httpMethod = httpMethod;
    }
    public String getReturns() {
        return returns;
    }

    public void setReturns(String returns) {
        this.returns = returns;
    }

    public List<ryz_Parameter> getRyz_parameters() {
        return ryz_parameters;
    }

    public void addRyz_parameter(Ryz_parameter ryz_parameter) {
        this.ryz_parameters.add(ryz_parameter);
    }

}