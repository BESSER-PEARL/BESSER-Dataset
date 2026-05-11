





import java.util.List;
import java.util.ArrayList;

public class aredsl_Tool  {

    private String description;
    private String precondition;
    private String id;
    private String targetPrecondition;





    private aredsl_ToolSet aredsl_toolset;


    public aredsl_Tool(
        String description,        String precondition,        String id,        String targetPrecondition    ) {
        this.description = description;
        this.precondition = precondition;
        this.id = id;
        this.targetPrecondition = targetPrecondition;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getPrecondition() {
        return precondition;
    }

    public void setPrecondition(String precondition) {
        this.precondition = precondition;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getTargetprecondition() {
        return targetPrecondition;
    }

    public void setTargetprecondition(String targetPrecondition) {
        this.targetPrecondition = targetPrecondition;
    }

    public aredsl_ToolSet getAredsl_toolset() {
        return aredsl_toolset;
    }

    public void setAredsl_toolset(aredsl_ToolSet aredsl_toolset) {
        this.aredsl_toolset = aredsl_toolset;
    }

}