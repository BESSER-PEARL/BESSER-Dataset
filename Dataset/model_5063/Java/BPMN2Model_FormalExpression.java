





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_FormalExpression extends Expression {

    private String body;
    private String mixed;
    private String language;





    private BPMN2Model_ItemDefinition bpmn2model_itemdefinition;




    private BPMN2Model_ComplexBehaviorDefinition bpmn2model_complexbehaviordefinition;




    private BPMN2Model_DataAssociation bpmn2model_dataassociation;




    private BPMN2Model_CorrelationPropertyBinding bpmn2model_correlationpropertybinding;




    private BPMN2Model_CorrelationPropertyRetrievalExpression bpmn2model_correlationpropertyretrievalexpression;


    public BPMN2Model_FormalExpression(
        String body,        String mixed,        String language    ) {
        super(
        );
        this.body = body;
        this.mixed = mixed;
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
    public String getLanguage() {
        return language;
    }

    public void setLanguage(String language) {
        this.language = language;
    }

    public BPMN2Model_ItemDefinition getBpmn2model_itemdefinition() {
        return bpmn2model_itemdefinition;
    }

    public void setBpmn2model_itemdefinition(BPMN2Model_ItemDefinition bpmn2model_itemdefinition) {
        this.bpmn2model_itemdefinition = bpmn2model_itemdefinition;
    }
    public BPMN2Model_ComplexBehaviorDefinition getBpmn2model_complexbehaviordefinition() {
        return bpmn2model_complexbehaviordefinition;
    }

    public void setBpmn2model_complexbehaviordefinition(BPMN2Model_ComplexBehaviorDefinition bpmn2model_complexbehaviordefinition) {
        this.bpmn2model_complexbehaviordefinition = bpmn2model_complexbehaviordefinition;
    }
    public BPMN2Model_DataAssociation getBpmn2model_dataassociation() {
        return bpmn2model_dataassociation;
    }

    public void setBpmn2model_dataassociation(BPMN2Model_DataAssociation bpmn2model_dataassociation) {
        this.bpmn2model_dataassociation = bpmn2model_dataassociation;
    }
    public BPMN2Model_CorrelationPropertyBinding getBpmn2model_correlationpropertybinding() {
        return bpmn2model_correlationpropertybinding;
    }

    public void setBpmn2model_correlationpropertybinding(BPMN2Model_CorrelationPropertyBinding bpmn2model_correlationpropertybinding) {
        this.bpmn2model_correlationpropertybinding = bpmn2model_correlationpropertybinding;
    }
    public BPMN2Model_CorrelationPropertyRetrievalExpression getBpmn2model_correlationpropertyretrievalexpression() {
        return bpmn2model_correlationpropertyretrievalexpression;
    }

    public void setBpmn2model_correlationpropertyretrievalexpression(BPMN2Model_CorrelationPropertyRetrievalExpression bpmn2model_correlationpropertyretrievalexpression) {
        this.bpmn2model_correlationpropertyretrievalexpression = bpmn2model_correlationpropertyretrievalexpression;
    }

}