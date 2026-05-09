





import java.util.List;
import java.util.ArrayList;

public class qvtrelationcs_ObjectTemplateCS extends TemplateCS {






    private List<qvtrelationcs_PropertyTemplateCS> qvtrelationcs_propertytemplatecss;




    private qvtrelationcs_PropertyTemplateCS qvtrelationcs_propertytemplatecs;


    public qvtrelationcs_ObjectTemplateCS(
    ) {
        super(
        );
        this.qvtrelationcs_propertytemplatecss = new ArrayList<>();
    }

    public qvtrelationcs_ObjectTemplateCS(
        ArrayList<qvtrelationcs_PropertyTemplateCS> qvtrelationcs_propertytemplatecss    ) {
        this.qvtrelationcs_propertytemplatecss = qvtrelationcs_propertytemplatecss;
    }


    public List<qvtrelationcs_PropertyTemplateCS> getQvtrelationcs_propertytemplatecss() {
        return qvtrelationcs_propertytemplatecss;
    }

    public void addQvtrelationcs_propertytemplatecs(Qvtrelationcs_propertytemplatecs qvtrelationcs_propertytemplatecs) {
        this.qvtrelationcs_propertytemplatecss.add(qvtrelationcs_propertytemplatecs);
    }
    public qvtrelationcs_PropertyTemplateCS getQvtrelationcs_propertytemplatecs() {
        return qvtrelationcs_propertytemplatecs;
    }

    public void setQvtrelationcs_propertytemplatecs(qvtrelationcs_PropertyTemplateCS qvtrelationcs_propertytemplatecs) {
        this.qvtrelationcs_propertytemplatecs = qvtrelationcs_propertytemplatecs;
    }

}