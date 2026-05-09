




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class esmodel_notification_ESNotification extends IdentifiableElement {

    private boolean seen;
    private String recipient;
    private String name;
    private String message;
    private String sender;
    private String details;
    private String provider;
    private LocalDate creationDate;





    private ProjectId projectid;




    private List<ModelElementId> modelelementids;




    private List<operations_OperationId> operations_operationids;


    public esmodel_notification_ESNotification(
        boolean seen,        String recipient,        String name,        String message,        String sender,        String details,        String provider,        LocalDate creationDate    ) {
        super(
        );
        this.seen = seen;
        this.recipient = recipient;
        this.name = name;
        this.message = message;
        this.sender = sender;
        this.details = details;
        this.provider = provider;
        this.creationDate = creationDate;
        this.modelelementids = new ArrayList<>();
        this.operations_operationids = new ArrayList<>();
    }

    public esmodel_notification_ESNotification(
        boolean seen,        String recipient,        String name,        String message,        String sender,        String details,        String provider,        LocalDate creationDate        ArrayList<ModelElementId> modelelementids,        ArrayList<operations_OperationId> operations_operationids    ) {
        this.seen = seen;
        this.recipient = recipient;
        this.name = name;
        this.message = message;
        this.sender = sender;
        this.details = details;
        this.provider = provider;
        this.creationDate = creationDate;
        this.modelelementids = modelelementids;
        this.operations_operationids = operations_operationids;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
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
    public LocalDate getCreationdate() {
        return creationDate;
    }

    public void setCreationdate(LocalDate creationDate) {
        this.creationDate = creationDate;
    }

    public ProjectId getProjectid() {
        return projectid;
    }

    public void setProjectid(ProjectId projectid) {
        this.projectid = projectid;
    }
    public List<ModelElementId> getModelelementids() {
        return modelelementids;
    }

    public void addModelelementid(Modelelementid modelelementid) {
        this.modelelementids.add(modelelementid);
    }
    public List<operations_OperationId> getOperations_operationids() {
        return operations_operationids;
    }

    public void addOperations_operationid(Operations_operationid operations_operationid) {
        this.operations_operationids.add(operations_operationid);
    }

}