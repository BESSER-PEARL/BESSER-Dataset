





import java.util.List;
import java.util.ArrayList;

public class bpmn2_FormalExpression extends Expression {

    private String language;
    private String body;
    private String mixed;





    private bpmn2_CorrelationPropertyBinding bpmn2_correlationpropertybinding;




    private bpmn2_CorrelationPropertyRetrievalExpression bpmn2_correlationpropertyretrievalexpression;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_ComplexBehaviorDefinition bpmn2_complexbehaviordefinition;




    private bpmn2_DataAssociation bpmn2_dataassociation;


    public bpmn2_FormalExpression(
        String language,        String body,        String mixed    ) {
        super(
        );
        this.language = language;
        this.body = body;
        this.mixed = mixed;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getMixed() {
        return mixed;
    }

    public void setMixed(String mixed) {
        this.mixed = mixed;
    }

    public bpmn2_CorrelationPropertyBinding getBpmn2_correlationpropertybinding() {
        return bpmn2_correlationpropertybinding;
    }

    public void setBpmn2_correlationpropertybinding(bpmn2_CorrelationPropertyBinding bpmn2_correlationpropertybinding) {
        this.bpmn2_correlationpropertybinding = bpmn2_correlationpropertybinding;
    }
    public bpmn2_CorrelationPropertyRetrievalExpression getBpmn2_correlationpropertyretrievalexpression() {
        return bpmn2_correlationpropertyretrievalexpression;
    }

    public void setBpmn2_correlationpropertyretrievalexpression(bpmn2_CorrelationPropertyRetrievalExpression bpmn2_correlationpropertyretrievalexpression) {
        this.bpmn2_correlationpropertyretrievalexpression = bpmn2_correlationpropertyretrievalexpression;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_ComplexBehaviorDefinition getBpmn2_complexbehaviordefinition() {
        return bpmn2_complexbehaviordefinition;
    }

    public void setBpmn2_complexbehaviordefinition(bpmn2_ComplexBehaviorDefinition bpmn2_complexbehaviordefinition) {
        this.bpmn2_complexbehaviordefinition = bpmn2_complexbehaviordefinition;
    }
    public bpmn2_DataAssociation getBpmn2_dataassociation() {
        return bpmn2_dataassociation;
    }

    public void setBpmn2_dataassociation(bpmn2_DataAssociation bpmn2_dataassociation) {
        this.bpmn2_dataassociation = bpmn2_dataassociation;
    }

}