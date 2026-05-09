





import java.util.List;
import java.util.ArrayList;

public class RootElement_Feedback  {

    private String feedbackDescription;
    private String read;
    private String rating;





    private RootElement_FeedbackHandler rootelement_feedbackhandler;


    public RootElement_Feedback(
        String feedbackDescription,        String read,        String rating    ) {
        this.feedbackDescription = feedbackDescription;
        this.read = read;
        this.rating = rating;
    }


    public String getFeedbackdescription() {
        return feedbackDescription;
    }

    public void setFeedbackdescription(String feedbackDescription) {
        this.feedbackDescription = feedbackDescription;
    }
    public String getRead() {
        return read;
    }

    public void setRead(String read) {
        this.read = read;
    }
    public String getRating() {
        return rating;
    }

    public void setRating(String rating) {
        this.rating = rating;
    }

    public RootElement_FeedbackHandler getRootelement_feedbackhandler() {
        return rootelement_feedbackhandler;
    }

    public void setRootelement_feedbackhandler(RootElement_FeedbackHandler rootelement_feedbackhandler) {
        this.rootelement_feedbackhandler = rootelement_feedbackhandler;
    }

}