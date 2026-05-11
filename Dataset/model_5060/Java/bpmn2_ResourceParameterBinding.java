





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ResourceParameterBinding  {

    private String id;





    private bpmn2_ResourceParameter bpmn2_resourceparameter;




    private bpmn2_ResourceRole bpmn2_resourcerole;




    private bpmn2_Expression bpmn2_expression;


    public bpmn2_ResourceParameterBinding(
        String id    ) {
        this.id = id;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public bpmn2_ResourceParameter getBpmn2_resourceparameter() {
        return bpmn2_resourceparameter;
    }

    public void setBpmn2_resourceparameter(bpmn2_ResourceParameter bpmn2_resourceparameter) {
        this.bpmn2_resourceparameter = bpmn2_resourceparameter;
    }
    public bpmn2_ResourceRole getBpmn2_resourcerole() {
        return bpmn2_resourcerole;
    }

    public void setBpmn2_resourcerole(bpmn2_ResourceRole bpmn2_resourcerole) {
        this.bpmn2_resourcerole = bpmn2_resourcerole;
    }
    public bpmn2_Expression getBpmn2_expression() {
        return bpmn2_expression;
    }

    public void setBpmn2_expression(bpmn2_Expression bpmn2_expression) {
        this.bpmn2_expression = bpmn2_expression;
    }

}