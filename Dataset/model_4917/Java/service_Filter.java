





import java.util.List;
import java.util.ArrayList;

public class service_Filter extends FormalParameterList, NamedDisplayElement {

    private String methodName;





    private service_Selection service_selection;




    private service_Selection service_selection;


    public service_Filter(
        String methodName    ) {
        super(
        );
        this.methodName = methodName;
    }


    public String getMethodname() {
        return methodName;
    }

    public void setMethodname(String methodName) {
        this.methodName = methodName;
    }

    public service_Selection getService_selection() {
        return service_selection;
    }

    public void setService_selection(service_Selection service_selection) {
        this.service_selection = service_selection;
    }
    public service_Selection getService_selection() {
        return service_selection;
    }

    public void setService_selection(service_Selection service_selection) {
        this.service_selection = service_selection;
    }

}