





import java.util.List;
import java.util.ArrayList;

public class Map_Address  {

    private String telephone;
    private String pictures;
    private String description;
    private boolean downtown;
    private float latitude;
    private float longitude;
    private String name;





    private Map_Map map_map;


    public Map_Address(
        String telephone,        String pictures,        String description,        boolean downtown,        float latitude,        float longitude,        String name    ) {
        this.telephone = telephone;
        this.pictures = pictures;
        this.description = description;
        this.downtown = downtown;
        this.latitude = latitude;
        this.longitude = longitude;
        this.name = name;
    }


    public String getTelephone() {
        return telephone;
    }

    public void setTelephone(String telephone) {
        this.telephone = telephone;
    }
    public String getPictures() {
        return pictures;
    }

    public void setPictures(String pictures) {
        this.pictures = pictures;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public boolean getDowntown() {
        return downtown;
    }

    public void setDowntown(boolean downtown) {
        this.downtown = downtown;
    }
    public float getLatitude() {
        return latitude;
    }

    public void setLatitude(float latitude) {
        this.latitude = latitude;
    }
    public float getLongitude() {
        return longitude;
    }

    public void setLongitude(float longitude) {
        this.longitude = longitude;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Map_Map getMap_map() {
        return map_map;
    }

    public void setMap_map(Map_Map map_map) {
        this.map_map = map_map;
    }

}