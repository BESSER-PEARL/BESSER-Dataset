





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_ToolFilterDescription  {

    private String precondition;
    private String elementsToListen;



    public viewpoint_tool_ToolFilterDescription(
        String precondition,        String elementsToListen    ) {
        this.precondition = precondition;
        this.elementsToListen = elementsToListen;
    }


    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getElementstolisten() {
        return elementsToListen;
    }

    public void setElementstolisten(String elementsToListen) {
        this.elementsToListen = elementsToListen;
    }


}