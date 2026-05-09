




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_notification_ESNotification extends IdentifiableElement {

    private String recipient;
    private String details;
    private LocalDate creationDate;
    private String provider;
    private String message;
    private String name;
    private boolean seen;
    private String sender;



    public esmodel_notification_ESNotification(
        String recipient,        String details,        LocalDate creationDate,        String provider,        String message,        String name,        boolean seen,        String sender    ) {
        super(
        );
        this.recipient = recipient;
        this.details = details;
        this.creationDate = creationDate;
        this.provider = provider;
        this.message = message;
        this.name = name;
        this.seen = seen;
        this.sender = sender;
    }


    public String getRecipient() {
        return recipient;
    }

    public void setRecipient(String recipient) {
        this.recipient = recipient;
    }
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
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
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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


}