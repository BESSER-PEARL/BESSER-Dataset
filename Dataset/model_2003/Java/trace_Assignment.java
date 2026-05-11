





import java.util.List;
import java.util.ArrayList;

public class trace_Assignment extends Step {

    private String assignmentType;
    private String id;
    private String displayName;
    private String baseName;





    private trace_Value trace_value;


    public trace_Assignment(
        String assignmentType,        String id,        String displayName,        String baseName    ) {
        super(
        );
        this.assignmentType = assignmentType;
        this.id = id;
        this.displayName = displayName;
        this.baseName = baseName;
    }


    public String getAssignmenttype() {
        return assignmentType;
    }

    public void setAssignmenttype(String assignmentType) {
        this.assignmentType = assignmentType;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getBasename() {
        return baseName;
    }

    public void setBasename(String baseName) {
        this.baseName = baseName;
    }

    public trace_Value getTrace_value() {
        return trace_value;
    }

    public void setTrace_value(trace_Value trace_value) {
        this.trace_value = trace_value;
    }

}