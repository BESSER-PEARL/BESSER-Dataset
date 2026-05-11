





import java.util.List;
import java.util.ArrayList;

public class metrics_RuleMetrics  {

    private int numberOfEdges;
    private int numberOfNodes;
    private int numberOfAttributes;





    private metrics_RuleSetMetrics metrics_rulesetmetrics;


    public metrics_RuleMetrics(
        int numberOfEdges,        int numberOfNodes,        int numberOfAttributes    ) {
        this.numberOfEdges = numberOfEdges;
        this.numberOfNodes = numberOfNodes;
        this.numberOfAttributes = numberOfAttributes;
    }


    public int getNumberofedges() {
        return numberOfEdges;
    }

    public void setNumberofedges(int numberOfEdges) {
        this.numberOfEdges = numberOfEdges;
    }
    public int getNumberofnodes() {
        return numberOfNodes;
    }

    public void setNumberofnodes(int numberOfNodes) {
        this.numberOfNodes = numberOfNodes;
    }
    public int getNumberofattributes() {
        return numberOfAttributes;
    }

    public void setNumberofattributes(int numberOfAttributes) {
        this.numberOfAttributes = numberOfAttributes;
    }

    public metrics_RuleSetMetrics getMetrics_rulesetmetrics() {
        return metrics_rulesetmetrics;
    }

    public void setMetrics_rulesetmetrics(metrics_RuleSetMetrics metrics_rulesetmetrics) {
        this.metrics_rulesetmetrics = metrics_rulesetmetrics;
    }

}