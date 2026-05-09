





import java.util.List;
import java.util.ArrayList;

public class graphpattern_AttributePattern extends GraphElement {

    private String constant;
    private String value;
    private String variables;





    private graphpattern_NodePattern graphpattern_nodepattern;




    private graphpattern_NodePattern graphpattern_nodepattern;


    public graphpattern_AttributePattern(
        String constant,        String value,        String variables    ) {
        super(
        );
        this.constant = constant;
        this.value = value;
        this.variables = variables;
    }


    public String getConstant() {
        return constant;
    }

    public void setConstant(String constant) {
        this.constant = constant;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getVariables() {
        return variables;
    }

    public void setVariables(String variables) {
        this.variables = variables;
    }

    public graphpattern_NodePattern getGraphpattern_nodepattern() {
        return graphpattern_nodepattern;
    }

    public void setGraphpattern_nodepattern(graphpattern_NodePattern graphpattern_nodepattern) {
        this.graphpattern_nodepattern = graphpattern_nodepattern;
    }
    public graphpattern_NodePattern getGraphpattern_nodepattern() {
        return graphpattern_nodepattern;
    }

    public void setGraphpattern_nodepattern(graphpattern_NodePattern graphpattern_nodepattern) {
        this.graphpattern_nodepattern = graphpattern_nodepattern;
    }

}