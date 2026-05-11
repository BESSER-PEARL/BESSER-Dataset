





import java.util.List;
import java.util.ArrayList;

public class sequence_description_MessageMapping extends description_EdgeMapping, description_EventMapping {

    private String sendingEndFinderExpression;
    private String receivingEndFinderExpression;



    public sequence_description_MessageMapping(
        String sendingEndFinderExpression,        String receivingEndFinderExpression    ) {
        super(
        );
        this.sendingEndFinderExpression = sendingEndFinderExpression;
        this.receivingEndFinderExpression = receivingEndFinderExpression;
    }


    public String getSendingendfinderexpression() {
        return sendingEndFinderExpression;
    }

    public void setSendingendfinderexpression(String sendingEndFinderExpression) {
        this.sendingEndFinderExpression = sendingEndFinderExpression;
    }
    public String getReceivingendfinderexpression() {
        return receivingEndFinderExpression;
    }

    public void setReceivingendfinderexpression(String receivingEndFinderExpression) {
        this.receivingEndFinderExpression = receivingEndFinderExpression;
    }


}