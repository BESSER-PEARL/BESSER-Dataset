





import java.util.List;
import java.util.ArrayList;

public class Advertiesment  {

    private String advertiser_id;
    private int advertiesment_id;
    private String end_date;
    private String start_date;





    private Advertiser advertiser;


    public Advertiesment(
        String advertiser_id,        int advertiesment_id,        String end_date,        String start_date    ) {
        this.advertiser_id = advertiser_id;
        this.advertiesment_id = advertiesment_id;
        this.end_date = end_date;
        this.start_date = start_date;
    }


    public String getAdvertiser_id() {
        return advertiser_id;
    }

    public void setAdvertiser_id(String advertiser_id) {
        this.advertiser_id = advertiser_id;
    }
    public int getAdvertiesment_id() {
        return advertiesment_id;
    }

    public void setAdvertiesment_id(int advertiesment_id) {
        this.advertiesment_id = advertiesment_id;
    }
    public String getEnd_date() {
        return end_date;
    }

    public void setEnd_date(String end_date) {
        this.end_date = end_date;
    }
    public String getStart_date() {
        return start_date;
    }

    public void setStart_date(String start_date) {
        this.start_date = start_date;
    }

    public Advertiser getAdvertiser() {
        return advertiser;
    }

    public void setAdvertiser(Advertiser advertiser) {
        this.advertiser = advertiser;
    }

}