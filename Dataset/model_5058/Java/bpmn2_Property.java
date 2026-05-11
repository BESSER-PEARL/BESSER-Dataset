





import java.util.List;
import java.util.ArrayList;

public class bpmn2_Property extends ItemAwareElement {

    private String name;





    private bpmn2_Process bpmn2_process;


    public bpmn2_Property(
        String name    ) {
        super(
        );
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public bpmn2_Process getBpmn2_process() {
        return bpmn2_process;
    }

    public void setBpmn2_process(bpmn2_Process bpmn2_process) {
        this.bpmn2_process = bpmn2_process;
    }

}