





import java.util.List;
import java.util.ArrayList;

public class sequence_description_MessageMapping extends description_EventMapping, description_EdgeMapping {

    private String receivingEndFinderExpression;
    private String sendingEndFinderExpression;



    public sequence_description_MessageMapping(
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