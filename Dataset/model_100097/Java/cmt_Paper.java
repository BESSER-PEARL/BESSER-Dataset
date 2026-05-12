





import java.util.List;
import java.util.ArrayList;

public class cmt_Paper extends Document {

    private String title;
    private String paperID;





    private Administrator administrator;




    private Reviewer reviewer;




    private Bid bid;




    private Reviewer reviewer;




    private Administrator administrator;


    public cmt_Paper(
        String title,        String paperID    ) {
        super(
        );
        this.title = title;
        this.paperID = paperID;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getPaperid() {
        return paperID;
    }

    public void setPaperid(String paperID) {
        this.paperID = paperID;
    }

    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }
    public Reviewer getReviewer() {
        return reviewer;
    }

    public void setReviewer(Reviewer reviewer) {
        this.reviewer = reviewer;
    }
    public Bid getBid() {
        return bid;
    }

    public void setBid(Bid bid) {
        this.bid = bid;
    }
    public Reviewer getReviewer() {
        return reviewer;
    }

    public void setReviewer(Reviewer reviewer) {
        this.reviewer = reviewer;
    }
    public Administrator getAdministrator() {
        return administrator;
    }

    public void setAdministrator(Administrator administrator) {
        this.administrator = administrator;
    }

}