





import java.util.List;
import java.util.ArrayList;

public class Position  {

    private int id;
    private String latitude;
    private String longitude;
    private String createdAt;





    private Buyer buyer;


    public Position(
        int id,        String latitude,        String longitude,        String createdAt    ) {
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
        this.createdAt = createdAt;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getLatitude() {
        return latitude;
    }

    public void setLatitude(String latitude) {
        this.latitude = latitude;
    }
    public String getLongitude() {
        return longitude;
    }

    public void setLongitude(String longitude) {
        this.longitude = longitude;
    }
    public String getCreatedat() {
        return createdAt;
    }

    public void setCreatedat(String createdAt) {
        this.createdAt = createdAt;
    }

    public Buyer getBuyer() {
        return buyer;
    }

    public void setBuyer(Buyer buyer) {
        this.buyer = buyer;
    }

}