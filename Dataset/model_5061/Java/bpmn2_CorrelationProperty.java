





import java.util.List;
import java.util.ArrayList;

public class bpmn2_CorrelationProperty extends RootElement {

    private String name;





    private bpmn2_CorrelationKey bpmn2_correlationkey;




    private List<bpmn2_CorrelationPropertyRetrievalExpression> bpmn2_correlationpropertyretrievalexpressions;




    private bpmn2_CorrelationPropertyBinding bpmn2_correlationpropertybinding;




    private bpmn2_ItemDefinition bpmn2_itemdefinition;


    public bpmn2_CorrelationProperty(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_correlationpropertyretrievalexpressions = new ArrayList<>();
    }

    public bpmn2_CorrelationProperty(
        String name        ArrayList<bpmn2_CorrelationPropertyRetrievalExpression> bpmn2_correlationpropertyretrievalexpressions    ) {
        this.name = name;
        this.bpmn2_correlationpropertyretrievalexpressions = bpmn2_correlationpropertyretrievalexpressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_CorrelationKey getBpmn2_correlationkey() {
        return bpmn2_correlationkey;
    }

    public void setBpmn2_correlationkey(bpmn2_CorrelationKey bpmn2_correlationkey) {
        this.bpmn2_correlationkey = bpmn2_correlationkey;
    }
    public List<bpmn2_CorrelationPropertyRetrievalExpression> getBpmn2_correlationpropertyretrievalexpressions() {
        return bpmn2_correlationpropertyretrievalexpressions;
    }

    public void addBpmn2_correlationpropertyretrievalexpression(Bpmn2_correlationpropertyretrievalexpression bpmn2_correlationpropertyretrievalexpression) {
        this.bpmn2_correlationpropertyretrievalexpressions.add(bpmn2_correlationpropertyretrievalexpression);
    }
    public bpmn2_CorrelationPropertyBinding getBpmn2_correlationpropertybinding() {
        return bpmn2_correlationpropertybinding;
    }

    public void setBpmn2_correlationpropertybinding(bpmn2_CorrelationPropertyBinding bpmn2_correlationpropertybinding) {
        this.bpmn2_correlationpropertybinding = bpmn2_correlationpropertybinding;
    }
    public bpmn2_ItemDefinition getBpmn2_itemdefinition() {
        return bpmn2_itemdefinition;
    }

    public void setBpmn2_itemdefinition(bpmn2_ItemDefinition bpmn2_itemdefinition) {
        this.bpmn2_itemdefinition = bpmn2_itemdefinition;
    }

}