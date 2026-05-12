





import java.util.List;
import java.util.ArrayList;

public class connection_ConceptTarget  {

    private String targetName;
    private String RelativeLoopExpression;





    private connection_Concept connection_concept;




    private connection_Concept connection_concept;


    public connection_ConceptTarget(
        String targetName,        String RelativeLoopExpression    ) {
        this.targetName = targetName;
        this.RelativeLoopExpression = RelativeLoopExpression;
    }


    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
    }
    public String getRelativeloopexpression() {
        return RelativeLoopExpression;
    }

    public void setRelativeloopexpression(String RelativeLoopExpression) {
        this.RelativeLoopExpression = RelativeLoopExpression;
    }

    public connection_Concept getConnection_concept() {
        return connection_concept;
    }

    public void setConnection_concept(connection_Concept connection_concept) {
        this.connection_concept = connection_concept;
    }
    public connection_Concept getConnection_concept() {
        return connection_concept;
    }

    public void setConnection_concept(connection_Concept connection_concept) {
        this.connection_concept = connection_concept;
    }

}