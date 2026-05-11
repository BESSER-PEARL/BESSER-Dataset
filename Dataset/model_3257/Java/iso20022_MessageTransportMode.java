





import java.util.List;
import java.util.ArrayList;

public class iso20022_MessageTransportMode extends TopLevelCatalogueEntry {

    private String messageDeliveryWindow;
    private String boundedCommunicationDelay;
    private String maximumMessageSize;
    private String messageDeliveryOrder;
    private String messageValidationOnOff;
    private String senderAsynchronicity;
    private String durability;
    private String messageCasting;
    private String messageSendingWindow;
    private String messageValidationLevel;
    private String deliveryAssurance;
    private String messageValidationResults;
    private String receiverAsynchronicity;
    private String maximumClockVariation;





    private List<iso20022_BusinessTransaction> iso20022_businesstransactions;




    private iso20022_BusinessTransaction iso20022_businesstransaction;


    public iso20022_MessageTransportMode(
        String messageDeliveryWindow,        String boundedCommunicationDelay,        String maximumMessageSize,        String messageDeliveryOrder,        String messageValidationOnOff,        String senderAsynchronicity,        String durability,        String messageCasting,        String messageSendingWindow,        String messageValidationLevel,        String deliveryAssurance,        String messageValidationResults,        String receiverAsynchronicity,        String maximumClockVariation    ) {
        super(
        );
        this.messageDeliveryWindow = messageDeliveryWindow;
        this.boundedCommunicationDelay = boundedCommunicationDelay;
        this.maximumMessageSize = maximumMessageSize;
        this.messageDeliveryOrder = messageDeliveryOrder;
        this.messageValidationOnOff = messageValidationOnOff;
        this.senderAsynchronicity = senderAsynchronicity;
        this.durability = durability;
        this.messageCasting = messageCasting;
        this.messageSendingWindow = messageSendingWindow;
        this.messageValidationLevel = messageValidationLevel;
        this.deliveryAssurance = deliveryAssurance;
        this.messageValidationResults = messageValidationResults;
        this.receiverAsynchronicity = receiverAsynchronicity;
        this.maximumClockVariation = maximumClockVariation;
        this.iso20022_businesstransactions = new ArrayList<>();
    }

    public iso20022_MessageTransportMode(
        String messageDeliveryWindow,        String boundedCommunicationDelay,        String maximumMessageSize,        String messageDeliveryOrder,        String messageValidationOnOff,        String senderAsynchronicity,        String durability,        String messageCasting,        String messageSendingWindow,        String messageValidationLevel,        String deliveryAssurance,        String messageValidationResults,        String receiverAsynchronicity,        String maximumClockVariation        ArrayList<iso20022_BusinessTransaction> iso20022_businesstransactions    ) {
        this.messageDeliveryWindow = messageDeliveryWindow;
        this.boundedCommunicationDelay = boundedCommunicationDelay;
        this.maximumMessageSize = maximumMessageSize;
        this.messageDeliveryOrder = messageDeliveryOrder;
        this.messageValidationOnOff = messageValidationOnOff;
        this.senderAsynchronicity = senderAsynchronicity;
        this.durability = durability;
        this.messageCasting = messageCasting;
        this.messageSendingWindow = messageSendingWindow;
        this.messageValidationLevel = messageValidationLevel;
        this.deliveryAssurance = deliveryAssurance;
        this.messageValidationResults = messageValidationResults;
        this.receiverAsynchronicity = receiverAsynchronicity;
        this.maximumClockVariation = maximumClockVariation;
        this.iso20022_businesstransactions = iso20022_businesstransactions;
    }

    public String getMessagedeliverywindow() {
        return messageDeliveryWindow;
    }

    public void setMessagedeliverywindow(String messageDeliveryWindow) {
        this.messageDeliveryWindow = messageDeliveryWindow;
    }
    public String getBoundedcommunicationdelay() {
        return boundedCommunicationDelay;
    }

    public void setBoundedcommunicationdelay(String boundedCommunicationDelay) {
        this.boundedCommunicationDelay = boundedCommunicationDelay;
    }
    public String getMaximummessagesize() {
        return maximumMessageSize;
    }

    public void setMaximummessagesize(String maximumMessageSize) {
        this.maximumMessageSize = maximumMessageSize;
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
    public String getSenderasynchronicity() {
        return senderAsynchronicity;
    }

    public void setSenderasynchronicity(String senderAsynchronicity) {
        this.senderAsynchronicity = senderAsynchronicity;
    }
    public String getDurability() {
        return durability;
    }

    public void setDurability(String durability) {
        this.durability = durability;
    }
    public String getMessagecasting() {
        return messageCasting;
    }

    public void setMessagecasting(String messageCasting) {
        this.messageCasting = messageCasting;
    }
    public String getMessagesendingwindow() {
        return messageSendingWindow;
    }

    public void setMessagesendingwindow(String messageSendingWindow) {
        this.messageSendingWindow = messageSendingWindow;
    }
    public String getMessagevalidationlevel() {
        return messageValidationLevel;
    }

    public void setMessagevalidationlevel(String messageValidationLevel) {
        this.messageValidationLevel = messageValidationLevel;
    }
    public String getDeliveryassurance() {
        return deliveryAssurance;
    }

    public void setDeliveryassurance(String deliveryAssurance) {
        this.deliveryAssurance = deliveryAssurance;
    }
    public String getMessagevalidationresults() {
        return messageValidationResults;
    }

    public void setMessagevalidationresults(String messageValidationResults) {
        this.messageValidationResults = messageValidationResults;
    }
    public String getReceiverasynchronicity() {
        return receiverAsynchronicity;
    }

    public void setReceiverasynchronicity(String receiverAsynchronicity) {
        this.receiverAsynchronicity = receiverAsynchronicity;
    }
    public String getMaximumclockvariation() {
        return maximumClockVariation;
    }

    public void setMaximumclockvariation(String maximumClockVariation) {
        this.maximumClockVariation = maximumClockVariation;
    }

    public List<iso20022_BusinessTransaction> getIso20022_businesstransactions() {
        return iso20022_businesstransactions;
    }

    public void addIso20022_businesstransaction(Iso20022_businesstransaction iso20022_businesstransaction) {
        this.iso20022_businesstransactions.add(iso20022_businesstransaction);
    }
    public iso20022_BusinessTransaction getIso20022_businesstransaction() {
        return iso20022_businesstransaction;
    }

    public void setIso20022_businesstransaction(iso20022_BusinessTransaction iso20022_businesstransaction) {
        this.iso20022_businesstransaction = iso20022_businesstransaction;
    }

}