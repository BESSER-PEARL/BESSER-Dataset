





import java.util.List;
import java.util.ArrayList;

public class reviews_Comment extends Indexed, Dated {

    private String id;
    private boolean draft;
    private String description;
    private String title;





    private List<reviews_Comment> reviews_comments;




    private reviews_CommentContainer reviews_commentcontainer;




    private reviews_CommentContainer reviews_commentcontainer;




    private reviews_CommentContainer reviews_commentcontainer;




    private reviews_CommentContainer reviews_commentcontainer;




    private reviews_CommentContainer reviews_commentcontainer;


    public reviews_Comment(
        String id,        boolean draft,        String description,        String title    ) {
        super(
        );
        this.id = id;
        this.draft = draft;
        this.description = description;
        this.title = title;
        this.reviews_comments = new ArrayList<>();
    }

    public reviews_Comment(
        String id,        boolean draft,        String description,        String title        ArrayList<reviews_Comment> reviews_comments    ) {
        this.id = id;
        this.draft = draft;
        this.description = description;
        this.title = title;
        this.reviews_comments = reviews_comments;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public boolean getDraft() {
        return draft;
    }

    public void setDraft(boolean draft) {
        this.draft = draft;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public List<reviews_Comment> getReviews_comments() {
        return reviews_comments;
    }

    public void addReviews_comment(Reviews_comment reviews_comment) {
        this.reviews_comments.add(reviews_comment);
    }
    public reviews_CommentContainer getReviews_commentcontainer() {
        return reviews_commentcontainer;
    }

    public void setReviews_commentcontainer(reviews_CommentContainer reviews_commentcontainer) {
        this.reviews_commentcontainer = reviews_commentcontainer;
    }
    public reviews_CommentContainer getReviews_commentcontainer() {
        return reviews_commentcontainer;
    }

    public void setReviews_commentcontainer(reviews_CommentContainer reviews_commentcontainer) {
        this.reviews_commentcontainer = reviews_commentcontainer;
    }
    public reviews_CommentContainer getReviews_commentcontainer() {
        return reviews_commentcontainer;
    }

    public void setReviews_commentcontainer(reviews_CommentContainer reviews_commentcontainer) {
        this.reviews_commentcontainer = reviews_commentcontainer;
    }
    public reviews_CommentContainer getReviews_commentcontainer() {
        return reviews_commentcontainer;
    }

    public void setReviews_commentcontainer(reviews_CommentContainer reviews_commentcontainer) {
        this.reviews_commentcontainer = reviews_commentcontainer;
    }
    public reviews_CommentContainer getReviews_commentcontainer() {
        return reviews_commentcontainer;
    }

    public void setReviews_commentcontainer(reviews_CommentContainer reviews_commentcontainer) {
        this.reviews_commentcontainer = reviews_commentcontainer;
    }

}