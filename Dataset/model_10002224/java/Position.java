





import java.util.List;
import java.util.ArrayList;

public class Position  {

    private String latitude;
    private String createdAt;
    private int id;
    private String longitude;





    private Buyer buyer;


    public Position(
        String latitude,        String createdAt,        int id,        String longitude    ) {
        this.latitude = latitude;
        this.createdAt = createdAt;
        this.id = id;
        this.longitude = longitude;
    }


    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }

    public Buyer getBuyer() {
        return buyer;
    }

    public void setBuyer(Buyer buyer) {
        this.buyer = buyer;
    }

}