





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageTransportMode extends TopLevelCatalogueEntry {

    private String messageSendingWindow;
    private String maximumMessageSize;
    private String receiverAsynchronicity;
    private String messageDeliveryOrder;
    private String messageValidationOnOff;
    private String boundedCommunicationDelay;
    private String messageCasting;
    private String durability;
    private String messageValidationResults;
    private String maximumClockVariation;
    private String messageValidationLevel;
    private String senderAsynchronicity;
    private String messageDeliveryWindow;
    private String deliveryAssurance;



    public iso20022_MessageTransportMode(
        String messageSendingWindow,        String maximumMessageSize,        String receiverAsynchronicity,        String messageDeliveryOrder,        String messageValidationOnOff,        String boundedCommunicationDelay,        String messageCasting,        String durability,        String messageValidationResults,        String maximumClockVariation,        String messageValidationLevel,        String senderAsynchronicity,        String messageDeliveryWindow,        String deliveryAssurance    ) {
        super(
        );
        this.messageSendingWindow = messageSendingWindow;
        this.maximumMessageSize = maximumMessageSize;
        this.receiverAsynchronicity = receiverAsynchronicity;
        this.messageDeliveryOrder = messageDeliveryOrder;
        this.messageValidationOnOff = messageValidationOnOff;
        this.boundedCommunicationDelay = boundedCommunicationDelay;
        this.messageCasting = messageCasting;
        this.durability = durability;
        this.messageValidationResults = messageValidationResults;
        this.maximumClockVariation = maximumClockVariation;
        this.messageValidationLevel = messageValidationLevel;
        this.senderAsynchronicity = senderAsynchronicity;
        this.messageDeliveryWindow = messageDeliveryWindow;
        this.deliveryAssurance = deliveryAssurance;
    }


    public String getMessagesendingwindow() {
        return messageSendingWindow;
    }

    public void setMessagesendingwindow(String messageSendingWindow) {
        this.messageSendingWindow = messageSendingWindow;
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
    public String getMessagedeliveryorder() {
        return messageDeliveryOrder;
    }

    public void setMessagedeliveryorder(String messageDeliveryOrder) {
        this.messageDeliveryOrder = messageDeliveryOrder;
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
    public String getMaximumclockvariation() {
        return maximumClockVariation;
    }

    public void setMaximumclockvariation(String maximumClockVariation) {
        this.maximumClockVariation = maximumClockVariation;
    }
    public String getMessagevalidationlevel() {
        return messageValidationLevel;
    }

    public void setMessagevalidationlevel(String messageValidationLevel) {
        this.messageValidationLevel = messageValidationLevel;
    }
    public String getSenderasynchronicity() {
        return senderAsynchronicity;
    }

    public void setSenderasynchronicity(String senderAsynchronicity) {
        this.senderAsynchronicity = senderAsynchronicity;
    }
    public String getMessagedeliverywindow() {
        return messageDeliveryWindow;
    }

    public void setMessagedeliverywindow(String messageDeliveryWindow) {
        this.messageDeliveryWindow = messageDeliveryWindow;
    }
    public String getDeliveryassurance() {
        return deliveryAssurance;
    }

    public void setDeliveryassurance(String deliveryAssurance) {
        this.deliveryAssurance = deliveryAssurance;
    }


}