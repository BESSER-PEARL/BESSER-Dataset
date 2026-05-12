





import java.util.List;
import java.util.ArrayList;

public class FollowUp  {

    private String stations;
    private String to;
    private boolean freePickup;
    private String name;
    private String password;
    private int type;
    private String from;
    private None driver;
    private String key;
    private String uid;
    private String info;
    private String time;



    public FollowUp(
        String stations,        String to,        boolean freePickup,        String name,        String password,        int type,        String from,        None driver,        String key,        String uid,        String info,        String time    ) {
        this.stations = stations;
        this.to = to;
        this.freePickup = freePickup;
        this.name = name;
        this.password = password;
        this.type = type;
        this.from = from;
        this.driver = driver;
        this.key = key;
        this.uid = uid;
        this.info = info;
        this.time = time;
    }


    public String getStations() {
        return stations;
    }

    public void setStations(String stations) {
        this.stations = stations;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public boolean getFreepickup() {
        return freePickup;
    }

    public void setFreepickup(boolean freePickup) {
        this.freePickup = freePickup;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getFrom() {
        return from;
    }

    public void setFrom(String from) {
        this.from = from;
    }
    public None getDriver() {
        return driver;
    }

    public void setDriver(None driver) {
        this.driver = driver;
    }
    public String getKey() {
        return key;
    }

    public void setKey(String key) {
        this.key = key;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }


}