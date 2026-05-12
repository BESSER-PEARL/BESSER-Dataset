





import java.util.List;
import java.util.ArrayList;

public class Position  {

    private int id;
    private String createdAt;
    private String longitude;
    private String latitude;





    private Buyer buyer;


    public Position(
        int id,        String createdAt,        String longitude,        String latitude    ) {
        this.id = id;
        this.createdAt = createdAt;
        this.longitude = longitude;
        this.latitude = latitude;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }
    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }
    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }

    public Buyer getBuyer() {
        return buyer;
    }

    public void setBuyer(Buyer buyer) {
        this.buyer = buyer;
    }

}