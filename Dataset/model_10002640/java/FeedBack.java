





import java.util.List;
import java.util.ArrayList;

public class FeedBack  {

    private String Rating;
    private String FeedBackMessage;





    private List<CheckOut_Entity> checkout_entitys;


    public FeedBack(
        String Rating,        String FeedBackMessage    ) {
        this.Rating = Rating;
        this.FeedBackMessage = FeedBackMessage;
        this.checkout_entitys = new ArrayList<>();
    }

    public FeedBack(
        String Rating,        String FeedBackMessage        ArrayList<CheckOut_Entity> checkout_entitys    ) {
        this.Rating = Rating;
        this.FeedBackMessage = FeedBackMessage;
        this.checkout_entitys = checkout_entitys;
    }

    public String getRating() {
        return Rating;
    }

    public void setRating(String Rating) {
        this.Rating = Rating;
    }
    public String getFeedbackmessage() {
        return FeedBackMessage;
    }

    public void setFeedbackmessage(String FeedBackMessage) {
        this.FeedBackMessage = FeedBackMessage;
    }

    public List<CheckOut_Entity> getCheckout_entitys() {
        return checkout_entitys;
    }

    public void addCheckout_entity(Checkout_entity checkout_entity) {
        this.checkout_entitys.add(checkout_entity);
    }

}