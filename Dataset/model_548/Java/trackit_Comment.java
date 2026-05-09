





import java.util.List;
import java.util.ArrayList;

public class trackit_Comment extends Identifiable {

    private String dateCreated;
    private String text;





    private trackit_Issue trackit_issue;




    private List<trackit_Comment> trackit_comments;




    private trackit_Comment trackit_comment;




    private trackit_Member trackit_member;




    private trackit_Issue trackit_issue;




    private trackit_Member trackit_member;


    public trackit_Comment(
        String dateCreated,        String text    ) {
        super(
        );
        this.dateCreated = dateCreated;
        this.text = text;
        this.trackit_comments = new ArrayList<>();
    }

    public trackit_Comment(
        String dateCreated,        String text        ArrayList<trackit_Comment> trackit_comments    ) {
        this.dateCreated = dateCreated;
        this.text = text;
        this.trackit_comments = trackit_comments;
    }

    public String getDatecreated() {
        return dateCreated;
    }

    public void setDatecreated(String dateCreated) {
        this.dateCreated = dateCreated;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public trackit_Issue getTrackit_issue() {
        return trackit_issue;
    }

    public void setTrackit_issue(trackit_Issue trackit_issue) {
        this.trackit_issue = trackit_issue;
    }
    public List<trackit_Comment> getTrackit_comments() {
        return trackit_comments;
    }

    public void addTrackit_comment(Trackit_comment trackit_comment) {
        this.trackit_comments.add(trackit_comment);
    }
    public trackit_Comment getTrackit_comment() {
        return trackit_comment;
    }

    public void setTrackit_comment(trackit_Comment trackit_comment) {
        this.trackit_comment = trackit_comment;
    }
    public trackit_Member getTrackit_member() {
        return trackit_member;
    }

    public void setTrackit_member(trackit_Member trackit_member) {
        this.trackit_member = trackit_member;
    }
    public trackit_Issue getTrackit_issue() {
        return trackit_issue;
    }

    public void setTrackit_issue(trackit_Issue trackit_issue) {
        this.trackit_issue = trackit_issue;
    }
    public trackit_Member getTrackit_member() {
        return trackit_member;
    }

    public void setTrackit_member(trackit_Member trackit_member) {
        this.trackit_member = trackit_member;
    }

}