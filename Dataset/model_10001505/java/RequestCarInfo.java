





import java.util.List;
import java.util.ArrayList;

public class RequestCarInfo  {

    private String from;
    private int type;
    private String to;
    private String time;
    private int numberOfDays;
    private String comment;
    private String uid;
    private int numberOfPassengers;
    private int state;
    private None user;



    public RequestCarInfo(
        String from,        int type,        String to,        String time,        int numberOfDays,        String comment,        String uid,        int numberOfPassengers,        int state,        None user    ) {
        this.from = from;
        this.type = type;
        this.to = to;
        this.time = time;
        this.numberOfDays = numberOfDays;
        this.comment = comment;
        this.uid = uid;
        this.numberOfPassengers = numberOfPassengers;
        this.state = state;
        this.user = user;
    }


    public String getFrom() {
        return from;
    }

    public void setFrom(String from) {
        this.from = from;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }
    public int getNumberofdays() {
        return numberOfDays;
    }

    public void setNumberofdays(int numberOfDays) {
        this.numberOfDays = numberOfDays;
    }
    public String getComment() {
        return comment;
    }

    public void setComment(String comment) {
        this.comment = comment;
    }
    public String getUid() {
        return uid;
    }

    public void setUid(String uid) {
        this.uid = uid;
    }
    public int getNumberofpassengers() {
        return numberOfPassengers;
    }

    public void setNumberofpassengers(int numberOfPassengers) {
        this.numberOfPassengers = numberOfPassengers;
    }
    public int getState() {
        return state;
    }

    public void setState(int state) {
        this.state = state;
    }
    public None getUser() {
        return user;
    }

    public void setUser(None user) {
        this.user = user;
    }


}