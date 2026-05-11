





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Message extends RootElement {






    private bpmn2_ItemDefinition bpmn2_itemdefinition;




    private bpmn2_CorrelationPropertyRetrievalExpression bpmn2_correlationpropertyretrievalexpression;




    private bpmn2_DocumentRoot bpmn2_documentroot;


    public bpmn2_Message(
    ) {
        super(
        );
    }



    public bpmn2_ItemDefinition getBpmn2_itemdefinition() {
        return bpmn2_itemdefinition;
    }

    public void setBpmn2_itemdefinition(bpmn2_ItemDefinition bpmn2_itemdefinition) {
        this.bpmn2_itemdefinition = bpmn2_itemdefinition;
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

}