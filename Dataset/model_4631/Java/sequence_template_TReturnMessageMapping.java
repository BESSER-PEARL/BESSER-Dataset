





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TReturnMessageMapping extends TMessageMapping {

    private String invocationMessageFinderExpression;



    public sequence_template_TReturnMessageMapping(
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