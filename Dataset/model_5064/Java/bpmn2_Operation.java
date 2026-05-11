





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Operation extends BaseElement {






    private bpmn2_Message bpmn2_message;




    private bpmn2_DocumentRoot bpmn2_documentroot;




    private bpmn2_Interface bpmn2_interface;




    private bpmn2_InputOutputBinding bpmn2_inputoutputbinding;




    private List<bpmn2_Error> bpmn2_errors;




    private bpmn2_Message bpmn2_message;




    private bpmn2_MessageEventDefinition bpmn2_messageeventdefinition;


    public bpmn2_Operation(
    ) {
        super(
        );
        this.bpmn2_errors = new ArrayList<>();
    }

    public bpmn2_Operation(
        ArrayList<bpmn2_Error> bpmn2_errors    ) {
        this.bpmn2_errors = bpmn2_errors;
    }


    public bpmn2_Message getBpmn2_message() {
        return bpmn2_message;
    }

    public void setBpmn2_message(bpmn2_Message bpmn2_message) {
        this.bpmn2_message = bpmn2_message;
    }
    public bpmn2_DocumentRoot getBpmn2_documentroot() {
        return bpmn2_documentroot;
    }

    public void setBpmn2_documentroot(bpmn2_DocumentRoot bpmn2_documentroot) {
        this.bpmn2_documentroot = bpmn2_documentroot;
    }
    public bpmn2_Interface getBpmn2_interface() {
        return bpmn2_interface;
    }

    public void setBpmn2_interface(bpmn2_Interface bpmn2_interface) {
        this.bpmn2_interface = bpmn2_interface;
    }
    public bpmn2_InputOutputBinding getBpmn2_inputoutputbinding() {
        return bpmn2_inputoutputbinding;
    }

    public void setBpmn2_inputoutputbinding(bpmn2_InputOutputBinding bpmn2_inputoutputbinding) {
        this.bpmn2_inputoutputbinding = bpmn2_inputoutputbinding;
    }
    public List<bpmn2_Error> getBpmn2_errors() {
        return bpmn2_errors;
    }

    public void addBpmn2_error(Bpmn2_error bpmn2_error) {
        this.bpmn2_errors.add(bpmn2_error);
    }
    public bpmn2_Message getBpmn2_message() {
        return bpmn2_message;
    }

    public void setBpmn2_message(bpmn2_Message bpmn2_message) {
        this.bpmn2_message = bpmn2_message;
    }
    public bpmn2_MessageEventDefinition getBpmn2_messageeventdefinition() {
        return bpmn2_messageeventdefinition;
    }

    public void setBpmn2_messageeventdefinition(bpmn2_MessageEventDefinition bpmn2_messageeventdefinition) {
        this.bpmn2_messageeventdefinition = bpmn2_messageeventdefinition;
    }

}