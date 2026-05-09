





import java.util.List;
import java.util.ArrayList;

public class project_JournalEntry extends ProjectAttribute, TaskAttribute, ResourceAttribute {

    private String headline;
    private String date;





    private project_Alert project_alert;




    private project_Summary project_summary;




    private project_Author project_author;




    private project_Details project_details;


    public project_JournalEntry(
        String headline,        String date    ) {
        super(
        );
        this.headline = headline;
        this.date = date;
    }


    public String getHeadline() {
        return headline;
    }

    public void setHeadline(String headline) {
        this.headline = headline;
    }
    public String getDate() {
        return date;
    }

    public void setDate(String date) {
        this.date = date;
    }

    public project_Alert getProject_alert() {
        return project_alert;
    }

    public void setProject_alert(project_Alert project_alert) {
        this.project_alert = project_alert;
    }
    public project_Summary getProject_summary() {
        return project_summary;
    }

    public void setProject_summary(project_Summary project_summary) {
        this.project_summary = project_summary;
    }
    public project_Author getProject_author() {
        return project_author;
    }

    public void setProject_author(project_Author project_author) {
        this.project_author = project_author;
    }
    public project_Details getProject_details() {
        return project_details;
    }

    public void setProject_details(project_Details project_details) {
        this.project_details = project_details;
    }

}