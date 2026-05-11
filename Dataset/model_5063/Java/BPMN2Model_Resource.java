





import java.util.List;
import java.util.ArrayList;

public class BPMN2Model_Resource extends RootElement {

    private String name;



    public BPMN2Model_Resource(
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