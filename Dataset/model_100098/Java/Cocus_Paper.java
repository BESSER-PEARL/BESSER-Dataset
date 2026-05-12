





import java.util.List;
import java.util.ArrayList;

public class Cocus_Paper extends Document {

    private String paperID;
    private String title;





    private Administrator administrator;




    private Reviewer reviewer;




    private Bid bid;




    private Reviewer reviewer;




    private Administrator administrator;




    private Decision decision;


    public Cocus_Paper(
        String paperID,        String title    ) {
        super(
        );
        this.paperID = paperID;
        this.title = title;
    }


    public String getPaperid() {
        return paperID;
    }

    public void setPaperid(String paperID) {
        this.paperID = paperID;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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
    public Decision getDecision() {
        return decision;
    }

    public void setDecision(Decision decision) {
        this.decision = decision;
    }

}