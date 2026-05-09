





import java.util.List;
import java.util.ArrayList;

public class graph_GEdge extends GModelElement {

    private String targetId;
    private String sourceId;
    private String routerKind;





    private graph_GModelElement graph_gmodelelement;




    private graph_GModelElement graph_gmodelelement;


    public graph_GEdge(
        String targetId,        String sourceId,        String routerKind    ) {
        super(
        );
        this.targetId = targetId;
        this.sourceId = sourceId;
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
    public String getRouterkind() {
        return routerKind;
    }

    public void setRouterkind(String routerKind) {
        this.routerKind = routerKind;
    }

    public graph_GModelElement getGraph_gmodelelement() {
        return graph_gmodelelement;
    }

    public void setGraph_gmodelelement(graph_GModelElement graph_gmodelelement) {
        this.graph_gmodelelement = graph_gmodelelement;
    }
    public graph_GModelElement getGraph_gmodelelement() {
        return graph_gmodelelement;
    }

    public void setGraph_gmodelelement(graph_GModelElement graph_gmodelelement) {
        this.graph_gmodelelement = graph_gmodelelement;
    }

}