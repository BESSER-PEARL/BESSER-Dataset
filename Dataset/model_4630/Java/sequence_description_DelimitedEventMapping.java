





import java.util.List;
import java.util.ArrayList;

public class sequence_description_DelimitedEventMapping extends EventMapping {

    private String finishingEndFinderExpression;
    private String startingEndFinderExpression;



    public sequence_description_DelimitedEventMapping(
        String finishingEndFinderExpression,        String startingEndFinderExpression    ) {
        super(
        );
        this.finishingEndFinderExpression = finishingEndFinderExpression;
        this.startingEndFinderExpression = startingEndFinderExpression;
    }


    public String getFinishingendfinderexpression() {
        return finishingEndFinderExpression;
    }

    public void setFinishingendfinderexpression(String finishingEndFinderExpression) {
        this.finishingEndFinderExpression = finishingEndFinderExpression;
    }
    public String getStartingendfinderexpression() {
        return startingEndFinderExpression;
    }

    public void setStartingendfinderexpression(String startingEndFinderExpression) {
        this.startingEndFinderExpression = startingEndFinderExpression;
    }


}