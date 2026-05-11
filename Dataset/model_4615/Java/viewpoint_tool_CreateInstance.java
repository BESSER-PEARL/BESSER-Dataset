





import java.util.List;
import java.util.ArrayList;

public class viewpoint_tool_CreateInstance extends ContainerModelOperation {

    private String variableName;
    private String typeName;
    private String referenceName;



    public viewpoint_tool_CreateInstance(
        String variableName,        String typeName,        String referenceName    ) {
        super(
        );
        this.variableName = variableName;
        this.typeName = typeName;
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
    public String getReferencename() {
        return referenceName;
    }

    public void setReferencename(String referenceName) {
        this.referenceName = referenceName;
    }


}