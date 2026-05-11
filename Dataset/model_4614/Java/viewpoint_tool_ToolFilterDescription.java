





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_ToolFilterDescription  {

    private String elementsToListen;
    private String precondition;



    public viewpoint_tool_ToolFilterDescription(
        String elementsToListen,        String precondition    ) {
        this.elementsToListen = elementsToListen;
        this.precondition = precondition;
    }


    public String getElementstolisten() {
        return elementsToListen;
    }

    public void setElementstolisten(String elementsToListen) {
        this.elementsToListen = elementsToListen;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }


}