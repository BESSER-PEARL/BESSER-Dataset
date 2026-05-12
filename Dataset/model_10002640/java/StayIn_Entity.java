





import java.util.List;
import java.util.ArrayList;

public class StayIn_Entity  {

    private None status;
    private String InPremisesList;
    private float placeOfInterest;
    private String promotionsList;
    private String oodList;
    private String EntertainMentList;





    private Payment payment;




    private CheckIn_Entity checkin_entity;


    public StayIn_Entity(
        None status,        String InPremisesList,        float placeOfInterest,        String promotionsList,        String oodList,        String EntertainMentList    ) {
        this.status = status;
        this.InPremisesList = InPremisesList;
        this.placeOfInterest = placeOfInterest;
        this.promotionsList = promotionsList;
        this.oodList = oodList;
        this.EntertainMentList = EntertainMentList;
    }


    public None getStatus() {
        return status;
    }

    public void setStatus(None status) {
        this.status = status;
    }
    public String getInpremiseslist() {
        return InPremisesList;
    }

    public void setInpremiseslist(String InPremisesList) {
        this.InPremisesList = InPremisesList;
    }
    public float getPlaceofinterest() {
        return placeOfInterest;
    }

    public void setPlaceofinterest(float placeOfInterest) {
        this.placeOfInterest = placeOfInterest;
    }
    public String getPromotionslist() {
        return promotionsList;
    }

    public void setPromotionslist(String promotionsList) {
        this.promotionsList = promotionsList;
    }
    public String getOodlist() {
        return oodList;
    }

    public void setOodlist(String oodList) {
        this.oodList = oodList;
    }
    public String getEntertainmentlist() {
        return EntertainMentList;
    }

    public void setEntertainmentlist(String EntertainMentList) {
        this.EntertainMentList = EntertainMentList;
    }

    public Payment getPayment() {
        return payment;
    }

    public void setPayment(Payment payment) {
        this.payment = payment;
    }
    public CheckIn_Entity getCheckin_entity() {
        return checkin_entity;
    }

    public void setCheckin_entity(CheckIn_Entity checkin_entity) {
        this.checkin_entity = checkin_entity;
    }

}