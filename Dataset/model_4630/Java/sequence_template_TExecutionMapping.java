





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TExecutionMapping extends template_TMessageExtremity, template_TAbstractMapping {

    private boolean recursive;
    private String startingEndFinderExpression;
    private String finishingEndFinderExpression;



    public sequence_template_TExecutionMapping(
        boolean recursive,        String startingEndFinderExpression,        String finishingEndFinderExpression    ) {
        super(
        );
        this.recursive = recursive;
        this.startingEndFinderExpression = startingEndFinderExpression;
        this.finishingEndFinderExpression = finishingEndFinderExpression;
    }


    public boolean getRecursive() {
        return recursive;
    }

    public void setRecursive(boolean recursive) {
        this.recursive = recursive;
    }
    public String getStartingendfinderexpression() {
        return startingEndFinderExpression;
    }

    public void setStartingendfinderexpression(String startingEndFinderExpression) {
        this.startingEndFinderExpression = startingEndFinderExpression;
    }
    public String getFinishingendfinderexpression() {
        return finishingEndFinderExpression;
    }

    public void setFinishingendfinderexpression(String finishingEndFinderExpression) {
        this.finishingEndFinderExpression = finishingEndFinderExpression;
    }


}