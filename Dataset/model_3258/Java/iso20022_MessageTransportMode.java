





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageTransportMode extends TopLevelCatalogueEntry {

    private String deliveryAssurance;
    private String senderAsynchronicity;
    private String messageDeliveryOrder;
    private String messageCasting;
    private String durability;
    private String messageValidationResults;
    private String maximumMessageSize;
    private String receiverAsynchronicity;
    private String messageSendingWindow;
    private String maximumClockVariation;
    private String messageValidationOnOff;
    private String boundedCommunicationDelay;
    private String messageDeliveryWindow;
    private String messageValidationLevel;



    public iso20022_MessageTransportMode(
        String deliveryAssurance,        String senderAsynchronicity,        String messageDeliveryOrder,        String messageCasting,        String durability,        String messageValidationResults,        String maximumMessageSize,        String receiverAsynchronicity,        String messageSendingWindow,        String maximumClockVariation,        String messageValidationOnOff,        String boundedCommunicationDelay,        String messageDeliveryWindow,        String messageValidationLevel    ) {
        super(
        );
        this.deliveryAssurance = deliveryAssurance;
        this.senderAsynchronicity = senderAsynchronicity;
        this.messageDeliveryOrder = messageDeliveryOrder;
        this.messageCasting = messageCasting;
        this.durability = durability;
        this.messageValidationResults = messageValidationResults;
        this.maximumMessageSize = maximumMessageSize;
        this.receiverAsynchronicity = receiverAsynchronicity;
        this.messageSendingWindow = messageSendingWindow;
        this.maximumClockVariation = maximumClockVariation;
        this.messageValidationOnOff = messageValidationOnOff;
        this.boundedCommunicationDelay = boundedCommunicationDelay;
        this.messageDeliveryWindow = messageDeliveryWindow;
        this.messageValidationLevel = messageValidationLevel;
    }


    public String getDeliveryassurance() {
        return deliveryAssurance;
    }

    public void setDeliveryassurance(String deliveryAssurance) {
        this.deliveryAssurance = deliveryAssurance;
    }
    public String getSenderasynchronicity() {
        return senderAsynchronicity;
    }

    public void setSenderasynchronicity(String senderAsynchronicity) {
        this.senderAsynchronicity = senderAsynchronicity;
    }
    public String getMessagedeliveryorder() {
        return messageDeliveryOrder;
    }

    public void setMessagedeliveryorder(String messageDeliveryOrder) {
        this.messageDeliveryOrder = messageDeliveryOrder;
    }
    public String getMessagecasting() {
        return messageCasting;
    }

    public void setMessagecasting(String messageCasting) {
        this.messageCasting = messageCasting;
    }
    public String getDurability() {
        return durability;
    }

    public void setDurability(String durability) {
        this.durability = durability;
    }
    public String getMessagevalidationresults() {
        return messageValidationResults;
    }

    public void setMessagevalidationresults(String messageValidationResults) {
        this.messageValidationResults = messageValidationResults;
    }
    public String getMaximummessagesize() {
        return maximumMessageSize;
    }

    public void setMaximummessagesize(String maximumMessageSize) {
        this.maximumMessageSize = maximumMessageSize;
    }
    public String getReceiverasynchronicity() {
        return receiverAsynchronicity;
    }

    public void setReceiverasynchronicity(String receiverAsynchronicity) {
        this.receiverAsynchronicity = receiverAsynchronicity;
    }
    public String getMessagesendingwindow() {
        return messageSendingWindow;
    }

    public void setMessagesendingwindow(String messageSendingWindow) {
        this.messageSendingWindow = messageSendingWindow;
    }
    public String getMaximumclockvariation() {
        return maximumClockVariation;
    }

    public void setMaximumclockvariation(String maximumClockVariation) {
        this.maximumClockVariation = maximumClockVariation;
    }
    public String getMessagevalidationonoff() {
        return messageValidationOnOff;
    }

    public void setMessagevalidationonoff(String messageValidationOnOff) {
        this.messageValidationOnOff = messageValidationOnOff;
    }
    public String getBoundedcommunicationdelay() {
        return boundedCommunicationDelay;
    }

    public void setBoundedcommunicationdelay(String boundedCommunicationDelay) {
        this.boundedCommunicationDelay = boundedCommunicationDelay;
    }
    public String getMessagedeliverywindow() {
        return messageDeliveryWindow;
    }

    public void setMessagedeliverywindow(String messageDeliveryWindow) {
        this.messageDeliveryWindow = messageDeliveryWindow;
    }
    public String getMessagevalidationlevel() {
        return messageValidationLevel;
    }

    public void setMessagevalidationlevel(String messageValidationLevel) {
        this.messageValidationLevel = messageValidationLevel;
    }


}