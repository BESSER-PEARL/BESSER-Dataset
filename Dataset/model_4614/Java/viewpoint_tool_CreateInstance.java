





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_CreateInstance extends ContainerModelOperation {

    private String referenceName;
    private String typeName;
    private String variableName;



    public viewpoint_tool_CreateInstance(
        String referenceName,        String typeName,        String variableName    ) {
        super(
        );
        this.referenceName = referenceName;
        this.typeName = typeName;
        this.variableName = variableName;
    }


    public String getReferencename() {
        return referenceName;
    }

    public void setReferencename(String referenceName) {
        this.referenceName = referenceName;
    }
    public String getTypename() {
        return typeName;
    }

    public void setTypename(String typeName) {
        this.typeName = typeName;
    }
    public String getVariablename() {
        return variableName;
    }

    public void setVariablename(String variableName) {
        this.variableName = variableName;
    }


}