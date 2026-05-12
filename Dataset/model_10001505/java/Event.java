





import java.util.List;
import java.util.ArrayList;

public class Event  {

    private String bannerUrl;
    private String endTime;
    private int type;
    private int freeSeats;
    private String price;
    private String eventPoints;
    private String uid;
    private String time;
    private String status;
    private String startTime;
    private String phoneNumber;
    private String name;
    private String info;



    public Event(
        String bannerUrl,        String endTime,        int type,        int freeSeats,        String price,        String eventPoints,        String uid,        String time,        String status,        String startTime,        String phoneNumber,        String name,        String info    ) {
        this.bannerUrl = bannerUrl;
        this.endTime = endTime;
        this.type = type;
        this.freeSeats = freeSeats;
        this.price = price;
        this.eventPoints = eventPoints;
        this.uid = uid;
        this.time = time;
        this.status = status;
        this.startTime = startTime;
        this.phoneNumber = phoneNumber;
        this.name = name;
        this.info = info;
    }


    public String getBannerurl() {
        return bannerUrl;
    }

    public void setBannerurl(String bannerUrl) {
        this.bannerUrl = bannerUrl;
    }
    public String getEndtime() {
        return endTime;
    }

    public void setEndtime(String endTime) {
        this.endTime = endTime;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public int getFreeseats() {
        return freeSeats;
    }

    public void setFreeseats(int freeSeats) {
        this.freeSeats = freeSeats;
    }
    public String getPrice() {
        return price;
    }

    public void setPrice(String price) {
        this.price = price;
    }
    public String getEventpoints() {
        return eventPoints;
    }

    public void setEventpoints(String eventPoints) {
        this.eventPoints = eventPoints;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getStarttime() {
        return startTime;
    }

    public void setStarttime(String startTime) {
        this.startTime = startTime;
    }
    public String getPhonenumber() {
        return phoneNumber;
    }

    public void setPhonenumber(String phoneNumber) {
        this.phoneNumber = phoneNumber;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }


}