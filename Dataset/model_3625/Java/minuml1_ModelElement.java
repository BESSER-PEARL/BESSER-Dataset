





import java.util.List;
import java.util.ArrayList;

public class minuml1_ModelElement  {

    private String name;





    private minuml1_ObjectFlowState minuml1_objectflowstate;


    public minuml1_ModelElement(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public minuml1_ObjectFlowState getMinuml1_objectflowstate() {
        return minuml1_objectflowstate;
    }

    public void setMinuml1_objectflowstate(minuml1_ObjectFlowState minuml1_objectflowstate) {
        this.minuml1_objectflowstate = minuml1_objectflowstate;
    }

}