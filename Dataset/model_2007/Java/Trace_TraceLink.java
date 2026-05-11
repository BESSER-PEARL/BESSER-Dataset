





import java.util.List;
import java.util.ArrayList;

public class Trace_TraceLink  {

    private String targetType;
    private String sourceName;
    private String sourceType;
    private String description;
    private String targetName;



    public Trace_TraceLink(
        String targetType,        String sourceName,        String sourceType,        String description,        String targetName    ) {
        this.targetType = targetType;
        this.sourceName = sourceName;
        this.sourceType = sourceType;
        this.description = description;
        this.targetName = targetName;
    }


    public String getTargettype() {
        return targetType;
    }

    public void setTargettype(String targetType) {
        this.targetType = targetType;
    }
    public String getSourcename() {
        return sourceName;
    }

    public void setSourcename(String sourceName) {
        this.sourceName = sourceName;
    }
    public String getSourcetype() {
        return sourceType;
    }

    public void setSourcetype(String sourceType) {
        this.sourceType = sourceType;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
    }


}