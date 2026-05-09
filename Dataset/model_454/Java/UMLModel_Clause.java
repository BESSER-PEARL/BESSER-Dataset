





import java.util.List;
import java.util.ArrayList;

public class UMLModel_Clause extends Element {

    private String test;
    private String decider;
    private String bodyOutput;
    private String successorClause;
    private String body;
    private String predecessorClause;





    private UMLModel_ConditionalNode umlmodel_conditionalnode;


    public UMLModel_Clause(
        String test,        String decider,        String bodyOutput,        String successorClause,        String body,        String predecessorClause    ) {
        super(
        );
        this.test = test;
        this.decider = decider;
        this.bodyOutput = bodyOutput;
        this.successorClause = successorClause;
        this.body = body;
        this.predecessorClause = predecessorClause;
    }


    public String getTest() {
        return test;
    }

    public void setTest(String test) {
        this.test = test;
    }
    public String getDecider() {
        return decider;
    }

    public void setDecider(String decider) {
        this.decider = decider;
    }
    public String getBodyoutput() {
        return bodyOutput;
    }

    public void setBodyoutput(String bodyOutput) {
        this.bodyOutput = bodyOutput;
    }
    public String getSuccessorclause() {
        return successorClause;
    }

    public void setSuccessorclause(String successorClause) {
        this.successorClause = successorClause;
    }
    public String getBody() {
        return body;
    }

    public void setBody(String body) {
        this.body = body;
    }
    public String getPredecessorclause() {
        return predecessorClause;
    }

    public void setPredecessorclause(String predecessorClause) {
        this.predecessorClause = predecessorClause;
    }

    public UMLModel_ConditionalNode getUmlmodel_conditionalnode() {
        return umlmodel_conditionalnode;
    }

    public void setUmlmodel_conditionalnode(UMLModel_ConditionalNode umlmodel_conditionalnode) {
        this.umlmodel_conditionalnode = umlmodel_conditionalnode;
    }

}