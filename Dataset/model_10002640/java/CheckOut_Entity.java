





import java.util.List;
import java.util.ArrayList;

public class CheckOut_Entity  {

    private float price;
    private None ItemisedBillDetails;





    private StayIn_Entity stayin_entity;




    private PostStay_Entity poststay_entity;




    private List<Payment> payments;


    public CheckOut_Entity(
        float price,        None ItemisedBillDetails    ) {
        this.price = price;
        this.ItemisedBillDetails = ItemisedBillDetails;
        this.payments = new ArrayList<>();
    }

    public CheckOut_Entity(
        float price,        None ItemisedBillDetails        ArrayList<Payment> payments    ) {
        this.price = price;
        this.ItemisedBillDetails = ItemisedBillDetails;
        this.payments = payments;
    }

    public float getPrice() {
        return price;
    }

    public void setPrice(float price) {
        this.price = price;
    }
    public None getItemisedbilldetails() {
        return ItemisedBillDetails;
    }

    public void setItemisedbilldetails(None ItemisedBillDetails) {
        this.ItemisedBillDetails = ItemisedBillDetails;
    }

    public StayIn_Entity getStayin_entity() {
        return stayin_entity;
    }

    public void setStayin_entity(StayIn_Entity stayin_entity) {
        this.stayin_entity = stayin_entity;
    }
    public PostStay_Entity getPoststay_entity() {
        return poststay_entity;
    }

    public void setPoststay_entity(PostStay_Entity poststay_entity) {
        this.poststay_entity = poststay_entity;
    }
    public List<Payment> getPayments() {
        return payments;
    }

    public void addPayment(Payment payment) {
        this.payments.add(payment);
    }

}