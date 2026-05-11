





import java.util.List;
import java.util.ArrayList;

public class sequence_template_TMessageMapping extends TAbstractMapping {

    private String receivingEndFinderExpression;
    private String sendingEndFinderExpression;



    public sequence_template_TMessageMapping(
        String receivingEndFinderExpression,        String sendingEndFinderExpression    ) {
        super(
        );
        this.receivingEndFinderExpression = receivingEndFinderExpression;
        this.sendingEndFinderExpression = sendingEndFinderExpression;
    }


    public String getReceivingendfinderexpression() {
        return receivingEndFinderExpression;
    }

    public void setReceivingendfinderexpression(String receivingEndFinderExpression) {
        this.receivingEndFinderExpression = receivingEndFinderExpression;
    }
    public String getSendingendfinderexpression() {
        return sendingEndFinderExpression;
    }

    public void setSendingendfinderexpression(String sendingEndFinderExpression) {
        this.sendingEndFinderExpression = sendingEndFinderExpression;
    }


}