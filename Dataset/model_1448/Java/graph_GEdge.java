





import java.util.List;
import java.util.ArrayList;

public class graph_GEdge extends GModelElement {

    private String routerKind;
    private String sourceId;
    private String targetId;



    public graph_GEdge(
        String routerKind,        String sourceId,        String targetId    ) {
        super(
        );
        this.routerKind = routerKind;
        this.sourceId = sourceId;
        this.targetId = targetId;
    }


    public String getRouterkind() {
        return routerKind;
    }

    public void setRouterkind(String routerKind) {
        this.routerKind = routerKind;
    }
    public String getSourceid() {
        return sourceId;
    }

    public void setSourceid(String sourceId) {
        this.sourceId = sourceId;
    }
    public String getTargetid() {
        return targetId;
    }

    public void setTargetid(String targetId) {
        this.targetId = targetId;
    }


}