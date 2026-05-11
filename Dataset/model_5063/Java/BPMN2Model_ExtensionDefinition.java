





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_ExtensionDefinition extends BPMNBase {

    private String name;



    public BPMN2Model_ExtensionDefinition(
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


}