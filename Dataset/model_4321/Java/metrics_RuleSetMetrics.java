





import java.util.List;
import java.util.ArrayList;

public class metrics_RuleSetMetrics  {

    private int totalNumberOfAttributes;
    private int numberOfRules;
    private int totalNumberOfEdges;
    private int totalNumberOfNodes;



    public metrics_RuleSetMetrics(
        int totalNumberOfAttributes,        int numberOfRules,        int totalNumberOfEdges,        int totalNumberOfNodes    ) {
        this.totalNumberOfAttributes = totalNumberOfAttributes;
        this.numberOfRules = numberOfRules;
        this.totalNumberOfEdges = totalNumberOfEdges;
        this.totalNumberOfNodes = totalNumberOfNodes;
    }


    public int getTotalnumberofattributes() {
        return totalNumberOfAttributes;
    }

    public void setTotalnumberofattributes(int totalNumberOfAttributes) {
        this.totalNumberOfAttributes = totalNumberOfAttributes;
    }
    public int getNumberofrules() {
        return numberOfRules;
    }

    public void setNumberofrules(int numberOfRules) {
        this.numberOfRules = numberOfRules;
    }
    public int getTotalnumberofedges() {
        return totalNumberOfEdges;
    }

    public void setTotalnumberofedges(int totalNumberOfEdges) {
        this.totalNumberOfEdges = totalNumberOfEdges;
    }
    public int getTotalnumberofnodes() {
        return totalNumberOfNodes;
    }

    public void setTotalnumberofnodes(int totalNumberOfNodes) {
        this.totalNumberOfNodes = totalNumberOfNodes;
    }


}