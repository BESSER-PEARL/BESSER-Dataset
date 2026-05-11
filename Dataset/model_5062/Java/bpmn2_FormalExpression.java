





import java.util.List;
import java.util.ArrayList;

public class bpmn2_FormalExpression extends Expression {

    private String language;





    private bpmn2_CorrelationPropertyRetrievalExpression bpmn2_correlationpropertyretrievalexpression;




    private bpmn2_CorrelationPropertyBinding bpmn2_correlationpropertybinding;




    private bpmn2_EObject bpmn2_eobject;




    private bpmn2_ComplexBehaviorDefinition bpmn2_complexbehaviordefinition;




    private bpmn2_ItemDefinition bpmn2_itemdefinition;




    private bpmn2_DataAssociation bpmn2_dataassociation;


    public bpmn2_FormalExpression(
        String language    ) {
        super(
        );
        this.language = language;
    }


    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public bpmn2_CorrelationPropertyRetrievalExpression getBpmn2_correlationpropertyretrievalexpression() {
        return bpmn2_correlationpropertyretrievalexpression;
    }

    public void setBpmn2_correlationpropertyretrievalexpression(bpmn2_CorrelationPropertyRetrievalExpression bpmn2_correlationpropertyretrievalexpression) {
        this.bpmn2_correlationpropertyretrievalexpression = bpmn2_correlationpropertyretrievalexpression;
    }
    public bpmn2_CorrelationPropertyBinding getBpmn2_correlationpropertybinding() {
        return bpmn2_correlationpropertybinding;
    }

    public void setBpmn2_correlationpropertybinding(bpmn2_CorrelationPropertyBinding bpmn2_correlationpropertybinding) {
        this.bpmn2_correlationpropertybinding = bpmn2_correlationpropertybinding;
    }
    public bpmn2_EObject getBpmn2_eobject() {
        return bpmn2_eobject;
    }

    public void setBpmn2_eobject(bpmn2_EObject bpmn2_eobject) {
        this.bpmn2_eobject = bpmn2_eobject;
    }
    public bpmn2_ComplexBehaviorDefinition getBpmn2_complexbehaviordefinition() {
        return bpmn2_complexbehaviordefinition;
    }

    public void setBpmn2_complexbehaviordefinition(bpmn2_ComplexBehaviorDefinition bpmn2_complexbehaviordefinition) {
        this.bpmn2_complexbehaviordefinition = bpmn2_complexbehaviordefinition;
    }
    public bpmn2_ItemDefinition getBpmn2_itemdefinition() {
        return bpmn2_itemdefinition;
    }

    public void setBpmn2_itemdefinition(bpmn2_ItemDefinition bpmn2_itemdefinition) {
        this.bpmn2_itemdefinition = bpmn2_itemdefinition;
    }
    public bpmn2_DataAssociation getBpmn2_dataassociation() {
        return bpmn2_dataassociation;
    }

    public void setBpmn2_dataassociation(bpmn2_DataAssociation bpmn2_dataassociation) {
        this.bpmn2_dataassociation = bpmn2_dataassociation;
    }

}