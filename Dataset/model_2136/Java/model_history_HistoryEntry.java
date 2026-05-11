





import java.util.List;
import java.util.ArrayList;

public class model_history_HistoryEntry  {

    private String timestamp;
    private String user;
    private String comment;
    private String deletedObjects;





    private List<Change> changes;


    public model_history_HistoryEntry(
        String timestamp,        String user,        String comment,        String deletedObjects    ) {
        this.timestamp = timestamp;
        this.user = user;
        this.comment = comment;
        this.deletedObjects = deletedObjects;
        this.changes = new ArrayList<>();
    }

    public model_history_HistoryEntry(
        String timestamp,        String user,        String comment,        String deletedObjects        ArrayList<Change> changes    ) {
        this.timestamp = timestamp;
        this.user = user;
        this.comment = comment;
        this.deletedObjects = deletedObjects;
        this.changes = changes;
    }

    public String getTimestamp() {
        return timestamp;
    }

    public void setTimestamp(String timestamp) {
        this.timestamp = timestamp;
    }
    public String getUser() {
        return user;
    }

    public void setUser(String user) {
        this.user = user;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getDeletedobjects() {
        return deletedObjects;
    }

    public void setDeletedobjects(String deletedObjects) {
        this.deletedObjects = deletedObjects;
    }

    public List<Change> getChanges() {
        return changes;
    }

    public void addChange(Change change) {
        this.changes.add(change);
    }

}