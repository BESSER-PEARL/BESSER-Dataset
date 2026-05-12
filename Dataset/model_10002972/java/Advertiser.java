





import java.util.List;
import java.util.ArrayList;

public class Advertiser  {

    private String advertiesment_id;
    private String advertiser_id;





    private List<Advertiesment> advertiesments;


    public Advertiser(
        String advertiesment_id,        String advertiser_id    ) {
        this.advertiesment_id = advertiesment_id;
        this.advertiser_id = advertiser_id;
        this.advertiesments = new ArrayList<>();
    }

    public Advertiser(
        String advertiesment_id,        String advertiser_id        ArrayList<Advertiesment> advertiesments    ) {
        this.advertiesment_id = advertiesment_id;
        this.advertiser_id = advertiser_id;
        this.advertiesments = advertiesments;
    }

    public String getAdvertiesment_id() {
        return advertiesment_id;
    }

    public void setAdvertiesment_id(String advertiesment_id) {
        this.advertiesment_id = advertiesment_id;
    }
    public String getAdvertiser_id() {
        return advertiser_id;
    }

    public void setAdvertiser_id(String advertiser_id) {
        this.advertiser_id = advertiser_id;
    }

    public List<Advertiesment> getAdvertiesments() {
        return advertiesments;
    }

    public void addAdvertiesment(Advertiesment advertiesment) {
        this.advertiesments.add(advertiesment);
    }

}