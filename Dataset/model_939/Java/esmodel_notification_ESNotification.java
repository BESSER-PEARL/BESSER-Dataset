




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_notification_ESNotification extends IdentifiableElement {

    private String provider;
    private boolean seen;
    private String recipient;
    private String message;
    private String sender;
    private LocalDate creationDate;
    private String details;
    private String name;





    private List<ModelElementId> modelelementids;




    private ProjectId projectid;


    public esmodel_notification_ESNotification(
        String provider,        boolean seen,        String recipient,        String message,        String sender,        LocalDate creationDate,        String details,        String name    ) {
        super(
        );
        this.provider = provider;
        this.seen = seen;
        this.recipient = recipient;
        this.message = message;
        this.sender = sender;
        this.creationDate = creationDate;
        this.details = details;
        this.name = name;
        this.modelelementids = new ArrayList<>();
    }

    public esmodel_notification_ESNotification(
        String provider,        boolean seen,        String recipient,        String message,        String sender,        LocalDate creationDate,        String details,        String name        ArrayList<ModelElementId> modelelementids    ) {
        this.provider = provider;
        this.seen = seen;
        this.recipient = recipient;
        this.message = message;
        this.sender = sender;
        this.creationDate = creationDate;
        this.details = details;
        this.name = name;
        this.modelelementids = modelelementids;
    }

    public String getProvider() {
        return provider;
    }

    public void setProvider(String provider) {
        this.provider = provider;
    }
    public boolean getSeen() {
        return seen;
    }

    public void setSeen(boolean seen) {
        this.seen = seen;
    }
    public String getRecipient() {
        return recipient;
    }

    public void setRecipient(String recipient) {
        this.recipient = recipient;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
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

    public List<ModelElementId> getModelelementids() {
        return modelelementids;
    }

    public void addModelelementid(Modelelementid modelelementid) {
        this.modelelementids.add(modelelementid);
    }
    public ProjectId getProjectid() {
        return projectid;
    }

    public void setProjectid(ProjectId projectid) {
        this.projectid = projectid;
    }

}