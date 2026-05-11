





import java.util.List;
import java.util.ArrayList;

public class DOT_Graph extends GraphElement {

    private String ratio;
    private String labelloc;
    private String ordering;
    private boolean center;
    private boolean concentrate;
    private String labeljust;
    private String rankDir;
    private float nodeSeparation;
    private boolean compound;
    private String boundingBox;
    private String size;
    private String type;



    public DOT_Graph(
        String ratio,        String labelloc,        String ordering,        boolean center,        boolean concentrate,        String labeljust,        String rankDir,        float nodeSeparation,        boolean compound,        String boundingBox,        String size,        String type    ) {
        super(
        );
        this.ratio = ratio;
        this.labelloc = labelloc;
        this.ordering = ordering;
        this.center = center;
        this.concentrate = concentrate;
        this.labeljust = labeljust;
        this.rankDir = rankDir;
        this.nodeSeparation = nodeSeparation;
        this.compound = compound;
        this.boundingBox = boundingBox;
        this.size = size;
        this.type = type;
    }


    public String getRatio() {
        return ratio;
    }

    public void setRatio(String ratio) {
        this.ratio = ratio;
    }
    public String getLabelloc() {
        return labelloc;
    }

    public void setLabelloc(String labelloc) {
        this.labelloc = labelloc;
    }
    public String getOrdering() {
        return ordering;
    }

    public void setOrdering(String ordering) {
        this.ordering = ordering;
    }
    public boolean getCenter() {
        return center;
    }

    public void setCenter(boolean center) {
        this.center = center;
    }
    public boolean getConcentrate() {
        return concentrate;
    }

    public void setConcentrate(boolean concentrate) {
        this.concentrate = concentrate;
    }
    public String getLabeljust() {
        return labeljust;
    }

    public void setLabeljust(String labeljust) {
        this.labeljust = labeljust;
    }
    public String getRankdir() {
        return rankDir;
    }

    public void setRankdir(String rankDir) {
        this.rankDir = rankDir;
    }
    public float getNodeseparation() {
        return nodeSeparation;
    }

    public void setNodeseparation(float nodeSeparation) {
        this.nodeSeparation = nodeSeparation;
    }
    public boolean getCompound() {
        return compound;
    }

    public void setCompound(boolean compound) {
        this.compound = compound;
    }
    public String getBoundingbox() {
        return boundingBox;
    }

    public void setBoundingbox(String boundingBox) {
        this.boundingBox = boundingBox;
    }
    public String getSize() {
        return size;
    }

    public void setSize(String size) {
        this.size = size;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}