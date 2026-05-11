





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Operation extends BaseElement {

    private String name;





    private bpmn2_Interface bpmn2_interface;




    private List<bpmn2_Error> bpmn2_errors;




    private bpmn2_Message bpmn2_message;




    private bpmn2_Message bpmn2_message;


    public bpmn2_Operation(
        String name    ) {
        super(
        );
        this.name = name;
        this.bpmn2_errors = new ArrayList<>();
    }

    public bpmn2_Operation(
        String name        ArrayList<bpmn2_Error> bpmn2_errors    ) {
        this.name = name;
        this.bpmn2_errors = bpmn2_errors;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_Interface getBpmn2_interface() {
        return bpmn2_interface;
    }

    public void setBpmn2_interface(bpmn2_Interface bpmn2_interface) {
        this.bpmn2_interface = bpmn2_interface;
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
    public bpmn2_Message getBpmn2_message() {
        return bpmn2_message;
    }

    public void setBpmn2_message(bpmn2_Message bpmn2_message) {
        this.bpmn2_message = bpmn2_message;
    }

}