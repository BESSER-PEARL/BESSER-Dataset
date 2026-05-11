





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Property extends ItemAwareElement {

    private String name;





    private BPMN2Model_Process bpmn2model_process;


    public BPMN2Model_Property(
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

    public BPMN2Model_Process getBpmn2model_process() {
        return bpmn2model_process;
    }

    public void setBpmn2model_process(BPMN2Model_Process bpmn2model_process) {
        this.bpmn2model_process = bpmn2model_process;
    }

}