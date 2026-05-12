





import java.util.List;
import java.util.ArrayList;

public class FEEDBACK_COMMENT  {

    private String userId;
    private int score;
    private String createdAt;
    private String comment;
    private String _id;
    private String feedbackId;





    private FEEDBACK feedback;


    public FEEDBACK_COMMENT(
        String userId,        int score,        String createdAt,        String comment,        String _id,        String feedbackId    ) {
        this.userId = userId;
        this.score = score;
        this.createdAt = createdAt;
        this.comment = comment;
        this._id = _id;
        this.feedbackId = feedbackId;
    }


    public String getUserid() {
        return userId;
    }

    public void setUserid(String userId) {
        this.userId = userId;
    }
    public int getScore() {
        return score;
    }

    public void setScore(int score) {
        this.score = score;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getFeedbackid() {
        return feedbackId;
    }

    public void setFeedbackid(String feedbackId) {
        this.feedbackId = feedbackId;
    }

    public FEEDBACK getFeedback() {
        return feedback;
    }

    public void setFeedback(FEEDBACK feedback) {
        this.feedback = feedback;
    }

}