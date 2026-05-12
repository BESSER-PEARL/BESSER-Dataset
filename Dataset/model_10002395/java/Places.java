




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class Places  {

    private String music;
    private String wifi;
    private String plugs;
    private String address;
    private int review_count;
    private String place_id;
    private int ID;
    private LocalDate opening_times;



    public Places(
        String music,        String wifi,        String plugs,        String address,        int review_count,        String place_id,        int ID,        LocalDate opening_times    ) {
        this.music = music;
        this.wifi = wifi;
        this.plugs = plugs;
        this.address = address;
        this.review_count = review_count;
        this.place_id = place_id;
        this.ID = ID;
        this.opening_times = opening_times;
    }


    public String getMusic() {
        return music;
    }

    public void setMusic(String music) {
        this.music = music;
    }
    public String getWifi() {
        return wifi;
    }

    public void setWifi(String wifi) {
        this.wifi = wifi;
    }
    public String getPlugs() {
        return plugs;
    }

    public void setPlugs(String plugs) {
        this.plugs = plugs;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getReview_count() {
        return review_count;
    }

    public void setReview_count(int review_count) {
        this.review_count = review_count;
    }
    public String getPlace_id() {
        return place_id;
    }

    public void setPlace_id(String place_id) {
        this.place_id = place_id;
    }
    public int getId() {
        return ID;
    }

    public void setId(int ID) {
        this.ID = ID;
    }
    public LocalDate getOpening_times() {
        return opening_times;
    }

    public void setOpening_times(LocalDate opening_times) {
        this.opening_times = opening_times;
    }


}