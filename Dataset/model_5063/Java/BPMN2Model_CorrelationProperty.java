





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_CorrelationProperty extends RootElement {

    private String name;





    private BPMN2Model_CorrelationKey bpmn2model_correlationkey;




    private BPMN2Model_ItemDefinition bpmn2model_itemdefinition;




    private BPMN2Model_CorrelationPropertyBinding bpmn2model_correlationpropertybinding;




    private List<BPMN2Model_CorrelationPropertyRetrievalExpression> bpmn2model_correlationpropertyretrievalexpressions;


    public BPMN2Model_CorrelationProperty(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2model_correlationpropertyretrievalexpressions = new ArrayList<>();
    }

    public BPMN2Model_CorrelationProperty(
        String name        ArrayList<BPMN2Model_CorrelationPropertyRetrievalExpression> bpmn2model_correlationpropertyretrievalexpressions    ) {
        this.name = name;
        this.bpmn2model_correlationpropertyretrievalexpressions = bpmn2model_correlationpropertyretrievalexpressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public BPMN2Model_CorrelationKey getBpmn2model_correlationkey() {
        return bpmn2model_correlationkey;
    }

    public void setBpmn2model_correlationkey(BPMN2Model_CorrelationKey bpmn2model_correlationkey) {
        this.bpmn2model_correlationkey = bpmn2model_correlationkey;
    }
    public BPMN2Model_ItemDefinition getBpmn2model_itemdefinition() {
        return bpmn2model_itemdefinition;
    }

    public void setBpmn2model_itemdefinition(BPMN2Model_ItemDefinition bpmn2model_itemdefinition) {
        this.bpmn2model_itemdefinition = bpmn2model_itemdefinition;
    }
    public BPMN2Model_CorrelationPropertyBinding getBpmn2model_correlationpropertybinding() {
        return bpmn2model_correlationpropertybinding;
    }

    public void setBpmn2model_correlationpropertybinding(BPMN2Model_CorrelationPropertyBinding bpmn2model_correlationpropertybinding) {
        this.bpmn2model_correlationpropertybinding = bpmn2model_correlationpropertybinding;
    }
    public List<BPMN2Model_CorrelationPropertyRetrievalExpression> getBpmn2model_correlationpropertyretrievalexpressions() {
        return bpmn2model_correlationpropertyretrievalexpressions;
    }

    public void addBpmn2model_correlationpropertyretrievalexpression(Bpmn2model_correlationpropertyretrievalexpression bpmn2model_correlationpropertyretrievalexpression) {
        this.bpmn2model_correlationpropertyretrievalexpressions.add(bpmn2model_correlationpropertyretrievalexpression);
    }

}