




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class btsviewmodel_StatusMessage  {

    private LocalDate creationTime;
    private String message;
    private String userId;
    private String messageType;





    private List<btsviewmodel_StatusMessage> btsviewmodel_statusmessages;


    public btsviewmodel_StatusMessage(
        LocalDate creationTime,        String message,        String userId,        String messageType    ) {
        this.creationTime = creationTime;
        this.message = message;
        this.userId = userId;
        this.messageType = messageType;
        this.btsviewmodel_statusmessages = new ArrayList<>();
    }

    public btsviewmodel_StatusMessage(
        LocalDate creationTime,        String message,        String userId,        String messageType        ArrayList<btsviewmodel_StatusMessage> btsviewmodel_statusmessages    ) {
        this.creationTime = creationTime;
        this.message = message;
        this.userId = userId;
        this.messageType = messageType;
        this.btsviewmodel_statusmessages = btsviewmodel_statusmessages;
    }

    public LocalDate getCreationtime() {
        return creationTime;
    }

    public void setCreationtime(LocalDate creationTime) {
        this.creationTime = creationTime;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public String getMessagetype() {
        return messageType;
    }

    public void setMessagetype(String messageType) {
        this.messageType = messageType;
    }

    public List<btsviewmodel_StatusMessage> getBtsviewmodel_statusmessages() {
        return btsviewmodel_statusmessages;
    }

    public void addBtsviewmodel_statusmessage(Btsviewmodel_statusmessage btsviewmodel_statusmessage) {
        this.btsviewmodel_statusmessages.add(btsviewmodel_statusmessage);
    }

}