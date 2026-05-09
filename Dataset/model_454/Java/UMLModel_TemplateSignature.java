





import java.util.List;
import java.util.ArrayList;

public class UMLModel_TemplateSignature extends Element {

    private String template;
    private String parameter;



    public UMLModel_TemplateSignature(
        String template,        String parameter    ) {
        super(
        );
        this.template = template;
        this.parameter = parameter;
    }


    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }
    public String getParameter() {
        return parameter;
    }

    public void setParameter(String parameter) {
        this.parameter = parameter;
    }


}