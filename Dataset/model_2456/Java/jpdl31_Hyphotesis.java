





import java.util.List;
import java.util.ArrayList;

public class jpdl31_Hyphotesis  {

    private String type;
    private String description;
    private String relationOp;
    private String id;





    private jpdl31_ExperimentalPlan jpdl31_experimentalplan;


    public jpdl31_Hyphotesis(
        String type,        String description,        String relationOp,        String id    ) {
        this.type = type;
        this.description = description;
        this.relationOp = relationOp;
        this.id = id;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getRelationop() {
        return relationOp;
    }

    public void setRelationop(String relationOp) {
        this.relationOp = relationOp;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public jpdl31_ExperimentalPlan getJpdl31_experimentalplan() {
        return jpdl31_experimentalplan;
    }

    public void setJpdl31_experimentalplan(jpdl31_ExperimentalPlan jpdl31_experimentalplan) {
        this.jpdl31_experimentalplan = jpdl31_experimentalplan;
    }

}