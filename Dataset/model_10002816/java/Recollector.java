





import java.util.List;
import java.util.ArrayList;

public class Recollector  {

    private String telephone;
    private String id;
    private String latitude;
    private String longitude;
    private String full_name;



    public Recollector(
        String telephone,        String id,        String latitude,        String longitude,        String full_name    ) {
        this.telephone = telephone;
        this.id = id;
        this.latitude = latitude;
        this.longitude = longitude;
        this.full_name = full_name;
    }


    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
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
    public String getFull_name() {
        return full_name;
    }

    public void setFull_name(String full_name) {
        this.full_name = full_name;
    }


}