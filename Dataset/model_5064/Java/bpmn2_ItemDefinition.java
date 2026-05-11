





import java.util.List;
import java.util.ArrayList;

public class bpmn2_ItemDefinition extends RootElement {

    private boolean isCollection;
    private String itemKind;





    private bpmn2_FormalExpression bpmn2_formalexpression;




    private bpmn2_Import bpmn2_import;




    private bpmn2_CorrelationProperty bpmn2_correlationproperty;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Error bpmn2_error;




    private bpmn2_Escalation bpmn2_escalation;


    public bpmn2_ItemDefinition(
        boolean isCollection,        String itemKind    ) {
        super(
        );
        this.isCollection = isCollection;
        this.itemKind = itemKind;
    }


    public boolean getIscollection() {
        return isCollection;
    }

    public void setIscollection(boolean isCollection) {
        this.isCollection = isCollection;
    }
    public String getItemkind() {
        return itemKind;
    }

    public void setItemkind(String itemKind) {
        this.itemKind = itemKind;
    }

    public bpmn2_FormalExpression getBpmn2_formalexpression() {
        return bpmn2_formalexpression;
    }

    public void setBpmn2_formalexpression(bpmn2_FormalExpression bpmn2_formalexpression) {
        this.bpmn2_formalexpression = bpmn2_formalexpression;
    }
    public bpmn2_Import getBpmn2_import() {
        return bpmn2_import;
    }

    public void setBpmn2_import(bpmn2_Import bpmn2_import) {
        this.bpmn2_import = bpmn2_import;
    }
    public bpmn2_CorrelationProperty getBpmn2_correlationproperty() {
        return bpmn2_correlationproperty;
    }

    public void setBpmn2_correlationproperty(bpmn2_CorrelationProperty bpmn2_correlationproperty) {
        this.bpmn2_correlationproperty = bpmn2_correlationproperty;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Error getBpmn2_error() {
        return bpmn2_error;
    }

    public void setBpmn2_error(bpmn2_Error bpmn2_error) {
        this.bpmn2_error = bpmn2_error;
    }
    public bpmn2_Escalation getBpmn2_escalation() {
        return bpmn2_escalation;
    }

    public void setBpmn2_escalation(bpmn2_Escalation bpmn2_escalation) {
        this.bpmn2_escalation = bpmn2_escalation;
    }

}