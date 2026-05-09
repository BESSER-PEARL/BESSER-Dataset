




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_notification_ESNotification extends IdentifiableElement {

    private String message;
    private boolean seen;
    private String sender;
    private String name;
    private String details;
    private String provider;
    private String recipient;
    private LocalDate creationDate;



    public esmodel_notification_ESNotification(
        String message,        boolean seen,        String sender,        String name,        String details,        String provider,        String recipient,        LocalDate creationDate    ) {
        super(
        );
        this.message = message;
        this.seen = seen;
        this.sender = sender;
        this.name = name;
        this.details = details;
        this.provider = provider;
        this.recipient = recipient;
        this.creationDate = creationDate;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
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
    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public String getRecipient() {
        return recipient;
    }

    public void setRecipient(String recipient) {
        this.recipient = recipient;
    }
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }


}