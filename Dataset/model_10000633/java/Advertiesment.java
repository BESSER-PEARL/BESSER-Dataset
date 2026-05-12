





import java.util.List;
import java.util.ArrayList;

public class Advertiesment  {

    private String advertiser_id;
    private String end_date;
    private int advertiesment_id;
    private String start_date;





    private Advertiser advertiser;


    public Advertiesment(
        String advertiser_id,        String end_date,        int advertiesment_id,        String start_date    ) {
        this.advertiser_id = advertiser_id;
        this.end_date = end_date;
        this.advertiesment_id = advertiesment_id;
        this.start_date = start_date;
    }


    public String getAdvertiser_id() {
        return advertiser_id;
    }

    public void setAdvertiser_id(String advertiser_id) {
        this.advertiser_id = advertiser_id;
    }
    public String getEnd_date() {
        return end_date;
    }

    public void setEnd_date(String end_date) {
        this.end_date = end_date;
    }
    public int getAdvertiesment_id() {
        return advertiesment_id;
    }

    public void setAdvertiesment_id(int advertiesment_id) {
        this.advertiesment_id = advertiesment_id;
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