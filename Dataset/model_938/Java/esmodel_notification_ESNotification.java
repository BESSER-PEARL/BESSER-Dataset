




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_notification_ESNotification extends IdentifiableElement {

    private String message;
    private LocalDate creationDate;
    private String provider;
    private String name;
    private String details;
    private boolean seen;
    private String sender;
    private String recipient;



    public esmodel_notification_ESNotification(
        String message,        LocalDate creationDate,        String provider,        String name,        String details,        boolean seen,        String sender,        String recipient    ) {
        super(
        );
        this.message = message;
        this.creationDate = creationDate;
        this.provider = provider;
        this.name = name;
        this.details = details;
        this.seen = seen;
        this.sender = sender;
        this.recipient = recipient;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
    }
    public boolean getSeen() {
        return seen;
    }

    public void setSeen(boolean seen) {
        this.seen = seen;
    }
    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }
    public String getRecipient() {
        return recipient;
    }

    public void setRecipient(String recipient) {
        this.recipient = recipient;
    }


}