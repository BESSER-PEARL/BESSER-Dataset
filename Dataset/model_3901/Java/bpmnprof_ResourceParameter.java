





import java.util.List;
import java.util.ArrayList;

public class bpmnprof_ResourceParameter extends BaseElement {

    private String isRequired;





    private bpmnprof_ResourceParameterBinding bpmnprof_resourceparameterbinding;


    public bpmnprof_ResourceParameter(
        String isRequired    ) {
        super(
        );
        this.isRequired = isRequired;
    }


    public String getIsrequired() {
        return isRequired;
    }

    public void setIsrequired(String isRequired) {
        this.isRequired = isRequired;
    }

    public bpmnprof_ResourceParameterBinding getBpmnprof_resourceparameterbinding() {
        return bpmnprof_resourceparameterbinding;
    }

    public void setBpmnprof_resourceparameterbinding(bpmnprof_ResourceParameterBinding bpmnprof_resourceparameterbinding) {
        this.bpmnprof_resourceparameterbinding = bpmnprof_resourceparameterbinding;
    }

}