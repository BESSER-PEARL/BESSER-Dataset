





import java.util.List;
import java.util.ArrayList;

public class connection_ConceptTarget  {

    private String RelativeLoopExpression;
    private String targetName;





    private connection_Concept connection_concept;




    private connection_Concept connection_concept;


    public connection_ConceptTarget(
        String RelativeLoopExpression,        String targetName    ) {
        this.RelativeLoopExpression = RelativeLoopExpression;
        this.targetName = targetName;
    }


    public String getRelativeloopexpression() {
        return RelativeLoopExpression;
    }

    public void setRelativeloopexpression(String RelativeLoopExpression) {
        this.RelativeLoopExpression = RelativeLoopExpression;
    }
    public String getTargetname() {
        return targetName;
    }

    public void setTargetname(String targetName) {
        this.targetName = targetName;
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