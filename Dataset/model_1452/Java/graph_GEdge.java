





import java.util.List;
import java.util.ArrayList;

public class graph_GEdge extends GModelElement {

    private String routerKind;
    private String targetId;
    private String sourceId;



    public graph_GEdge(
        String routerKind,        String targetId,        String sourceId    ) {
        super(
        );
        this.routerKind = routerKind;
        this.targetId = targetId;
        this.sourceId = sourceId;
    }


    public String getRouterkind() {
        return routerKind;
    }

    public void setRouterkind(String routerKind) {
        this.routerKind = routerKind;
    }
    public String getTargetid() {
        return targetId;
    }

    public void setTargetid(String targetId) {
        this.targetId = targetId;
    }
    public String getSourceid() {
        return sourceId;
    }

    public void setSourceid(String sourceId) {
        this.sourceId = sourceId;
    }


}