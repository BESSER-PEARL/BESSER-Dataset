




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_notification_ESNotification extends IdentifiableElement {

    private String provider;
    private String recipient;
    private LocalDate creationDate;
    private boolean seen;
    private String details;
    private String message;
    private String name;
    private String sender;



    public esmodel_notification_ESNotification(
        String provider,        String recipient,        LocalDate creationDate,        boolean seen,        String details,        String message,        String name,        String sender    ) {
        super(
        );
        this.provider = provider;
        this.recipient = recipient;
        this.creationDate = creationDate;
        this.seen = seen;
        this.details = details;
        this.message = message;
        this.name = name;
        this.sender = sender;
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
    public boolean getSeen() {
        return seen;
    }

    public void setSeen(boolean seen) {
        this.seen = seen;
    }
    public String getDetails() {
        return details;
    }

    public void setDetails(String details) {
        this.details = details;
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
    public String getSender() {
        return sender;
    }

    public void setSender(String sender) {
        this.sender = sender;
    }


}