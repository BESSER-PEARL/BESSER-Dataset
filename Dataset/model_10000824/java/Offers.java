





import java.util.List;
import java.util.ArrayList;

public class Offers  {

    private String Offer_Det;
    private String Offer_NO;
    private String Offer_Expiry_Date;





    private Passengers passengers;


    public Offers(
        String Offer_Det,        String Offer_NO,        String Offer_Expiry_Date    ) {
        this.Offer_Det = Offer_Det;
        this.Offer_NO = Offer_NO;
        this.Offer_Expiry_Date = Offer_Expiry_Date;
    }


    public String getOffer_det() {
        return Offer_Det;
    }

    public void setOffer_det(String Offer_Det) {
        this.Offer_Det = Offer_Det;
    }
    public String getOffer_no() {
        return Offer_NO;
    }

    public void setOffer_no(String Offer_NO) {
        this.Offer_NO = Offer_NO;
    }
    public String getOffer_expiry_date() {
        return Offer_Expiry_Date;
    }

    public void setOffer_expiry_date(String Offer_Expiry_Date) {
        this.Offer_Expiry_Date = Offer_Expiry_Date;
    }

    public Passengers getPassengers() {
        return passengers;
    }

    public void setPassengers(Passengers passengers) {
        this.passengers = passengers;
    }

}