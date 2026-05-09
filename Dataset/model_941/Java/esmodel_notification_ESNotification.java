




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_notification_ESNotification extends IdentifiableElement {

    private boolean seen;
    private String message;
    private String details;
    private String name;
    private String recipient;
    private String sender;
    private LocalDate creationDate;
    private String provider;



    public esmodel_notification_ESNotification(
        boolean seen,        String message,        String details,        String name,        String recipient,        String sender,        LocalDate creationDate,        String provider    ) {
        super(
        );
        this.seen = seen;
        this.message = message;
        this.details = details;
        this.name = name;
        this.recipient = recipient;
        this.sender = sender;
        this.creationDate = creationDate;
        this.provider = provider;
    }


    public boolean getSeen() {
        return seen;
    }

    public void setSeen(boolean seen) {
        this.seen = seen;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getRecipient() {
        return recipient;
    }

    public void setRecipient(String recipient) {
        this.recipient = recipient;
    }
    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }


}