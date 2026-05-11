





import java.util.List;
import java.util.ArrayList;

public class builds_Change  {

    private String message;
    private String date;
    private String revision;





    private builds_ChangeSet builds_changeset;




    private builds_User builds_user;


    public builds_Change(
        String message,        String date,        String revision    ) {
        this.message = message;
        this.date = date;
        this.revision = revision;
    }


    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }
    public String getRevision() {
        return revision;
    }

    public void setRevision(String revision) {
        this.revision = revision;
    }

    public builds_ChangeSet getBuilds_changeset() {
        return builds_changeset;
    }

    public void setBuilds_changeset(builds_ChangeSet builds_changeset) {
        this.builds_changeset = builds_changeset;
    }
    public builds_User getBuilds_user() {
        return builds_user;
    }

    public void setBuilds_user(builds_User builds_user) {
        this.builds_user = builds_user;
    }

}