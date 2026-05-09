





import java.util.List;
import java.util.ArrayList;

public class graphdom_Node  {

    private boolean dominated;
    private String color;
    private String nodeName;
    private int xCoord;
    private int yCoord;
    private String grade;
    private String guid;
    private boolean dominating;





    private graphdom_Graph graphdom_graph;


    public graphdom_Node(
        boolean dominated,        String color,        String nodeName,        int xCoord,        int yCoord,        String grade,        String guid,        boolean dominating    ) {
        this.dominated = dominated;
        this.color = color;
        this.nodeName = nodeName;
        this.xCoord = xCoord;
        this.yCoord = yCoord;
        this.grade = grade;
        this.guid = guid;
        this.dominating = dominating;
    }


    public boolean getDominated() {
        return dominated;
    }

    public void setDominated(boolean dominated) {
        this.dominated = dominated;
    }
    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }
    public String getNodename() {
        return nodeName;
    }

    public void setNodename(String nodeName) {
        this.nodeName = nodeName;
    }
    public int getXcoord() {
        return xCoord;
    }

    public void setXcoord(int xCoord) {
        this.xCoord = xCoord;
    }
    public int getYcoord() {
        return yCoord;
    }

    public void setYcoord(int yCoord) {
        this.yCoord = yCoord;
    }
    public String getGrade() {
        return grade;
    }

    public void setGrade(String grade) {
        this.grade = grade;
    }
    public String getGuid() {
        return guid;
    }

    public void setGuid(String guid) {
        this.guid = guid;
    }
    public boolean getDominating() {
        return dominating;
    }

    public void setDominating(boolean dominating) {
        this.dominating = dominating;
    }

    public graphdom_Graph getGraphdom_graph() {
        return graphdom_graph;
    }

    public void setGraphdom_graph(graphdom_Graph graphdom_graph) {
        this.graphdom_graph = graphdom_graph;
    }

}