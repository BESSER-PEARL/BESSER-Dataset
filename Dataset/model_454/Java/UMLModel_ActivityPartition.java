





import java.util.List;
import java.util.ArrayList;

public class UMLModel_ActivityPartition extends NamedElement, ActivityGroup {

    private String edge;
    private String represents;
    private String isDimension;
    private String node;
    private String subpartition;
    private String isExternal;
    private String superPartition;



    public UMLModel_ActivityPartition(
        String edge,        String represents,        String isDimension,        String node,        String subpartition,        String isExternal,        String superPartition    ) {
        super(
        );
        this.edge = edge;
        this.represents = represents;
        this.isDimension = isDimension;
        this.node = node;
        this.subpartition = subpartition;
        this.isExternal = isExternal;
        this.superPartition = superPartition;
    }


    public String getEdge() {
        return edge;
    }

    public void setEdge(String edge) {
        this.edge = edge;
    }
    public String getRepresents() {
        return represents;
    }

    public void setRepresents(String represents) {
        this.represents = represents;
    }
    public String getIsdimension() {
        return isDimension;
    }

    public void setIsdimension(String isDimension) {
        this.isDimension = isDimension;
    }
    public String getNode() {
        return node;
    }

    public void setNode(String node) {
        this.node = node;
    }
    public String getSubpartition() {
        return subpartition;
    }

    public void setSubpartition(String subpartition) {
        this.subpartition = subpartition;
    }
    public String getIsexternal() {
        return isExternal;
    }

    public void setIsexternal(String isExternal) {
        this.isExternal = isExternal;
    }
    public String getSuperpartition() {
        return superPartition;
    }

    public void setSuperpartition(String superPartition) {
        this.superPartition = superPartition;
    }


}