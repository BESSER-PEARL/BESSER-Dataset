





import java.util.List;
import java.util.ArrayList;

public class sequence_description_ReturnMessageMapping extends MessageMapping {

    private String invocationMessageFinderExpression;



    public sequence_description_ReturnMessageMapping(
        String invocationMessageFinderExpression    ) {
        super(
        );
        this.invocationMessageFinderExpression = invocationMessageFinderExpression;
    }


    public String getInvocationmessagefinderexpression() {
        return invocationMessageFinderExpression;
    }

    public void setInvocationmessagefinderexpression(String invocationMessageFinderExpression) {
        this.invocationMessageFinderExpression = invocationMessageFinderExpression;
    }


}