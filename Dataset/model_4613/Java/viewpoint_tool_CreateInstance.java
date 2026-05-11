





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_CreateInstance extends ContainerModelOperation {

    private String referenceName;
    private String variableName;
    private String typeName;



    public viewpoint_tool_CreateInstance(
        String referenceName,        String variableName,        String typeName    ) {
        super(
        );
        this.referenceName = referenceName;
        this.variableName = variableName;
        this.typeName = typeName;
    }


    public String getReferencename() {
        return referenceName;
    }

    public void setReferencename(String referenceName) {
        this.referenceName = referenceName;
    }
    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }


}