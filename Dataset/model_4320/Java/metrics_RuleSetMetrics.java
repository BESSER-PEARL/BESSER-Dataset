





import java.util.List;
import java.util.ArrayList;

public class metrics_RuleSetMetrics  {

    private int totalNumberOfEdges;
    private int numberOfRules;
    private int totalNumberOfNodes;
    private int totalNumberOfAttributes;



    public metrics_RuleSetMetrics(
        int totalNumberOfEdges,        int numberOfRules,        int totalNumberOfNodes,        int totalNumberOfAttributes    ) {
        this.totalNumberOfEdges = totalNumberOfEdges;
        this.numberOfRules = numberOfRules;
        this.totalNumberOfNodes = totalNumberOfNodes;
        this.totalNumberOfAttributes = totalNumberOfAttributes;
    }


    public int getTotalnumberofedges() {
        return totalNumberOfEdges;
    }

    public void setTotalnumberofedges(int totalNumberOfEdges) {
        this.totalNumberOfEdges = totalNumberOfEdges;
    }
    public int getNumberofrules() {
        return numberOfRules;
    }

    public void setNumberofrules(int numberOfRules) {
        this.numberOfRules = numberOfRules;
    }
    public int getTotalnumberofnodes() {
        return totalNumberOfNodes;
    }

    public void setTotalnumberofnodes(int totalNumberOfNodes) {
        this.totalNumberOfNodes = totalNumberOfNodes;
    }
    public int getTotalnumberofattributes() {
        return totalNumberOfAttributes;
    }

    public void setTotalnumberofattributes(int totalNumberOfAttributes) {
        this.totalNumberOfAttributes = totalNumberOfAttributes;
    }


}