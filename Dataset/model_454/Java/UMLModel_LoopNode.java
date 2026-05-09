





import java.util.List;
import java.util.ArrayList;

public class UMLModel_LoopNode extends StructuredActivityNode {

    private String setupPart;
    private String decider;
    private String isTestedFirst;
    private String bodyOutput;
    private String bodyPart;
    private String test;
    private String loopVariable;



    public UMLModel_LoopNode(
        String setupPart,        String decider,        String isTestedFirst,        String bodyOutput,        String bodyPart,        String test,        String loopVariable    ) {
        super(
        );
        this.setupPart = setupPart;
        this.decider = decider;
        this.isTestedFirst = isTestedFirst;
        this.bodyOutput = bodyOutput;
        this.bodyPart = bodyPart;
        this.test = test;
        this.loopVariable = loopVariable;
    }


    public String getSetuppart() {
        return setupPart;
    }

    public void setSetuppart(String setupPart) {
        this.setupPart = setupPart;
    }
    public String getDecider() {
        return decider;
    }

    public void setDecider(String decider) {
        this.decider = decider;
    }
    public String getIstestedfirst() {
        return isTestedFirst;
    }

    public void setIstestedfirst(String isTestedFirst) {
        this.isTestedFirst = isTestedFirst;
    }
    public String getBodyoutput() {
        return bodyOutput;
    }

    public void setBodyoutput(String bodyOutput) {
        this.bodyOutput = bodyOutput;
    }
    public String getBodypart() {
        return bodyPart;
    }

    public void setBodypart(String bodyPart) {
        this.bodyPart = bodyPart;
    }
    public String getTest() {
        return test;
    }

    public void setTest(String test) {
        this.test = test;
    }
    public String getLoopvariable() {
        return loopVariable;
    }

    public void setLoopvariable(String loopVariable) {
        this.loopVariable = loopVariable;
    }


}