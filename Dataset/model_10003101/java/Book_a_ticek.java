





import java.util.List;
import java.util.ArrayList;

public class Book_a_ticek  {

    private String time_;
    private String destination_city;
    private String ticket_id_;
    private String date_;
    private String starting_city_;





    private Pay pay;


    public Book_a_ticek(
        String time_,        String destination_city,        String ticket_id_,        String date_,        String starting_city_    ) {
        this.time_ = time_;
        this.destination_city = destination_city;
        this.ticket_id_ = ticket_id_;
        this.date_ = date_;
        this.starting_city_ = starting_city_;
    }


    public String getTime_() {
        return time_;
    }

    public void setTime_(String time_) {
        this.time_ = time_;
    }
    public String getDestination_city() {
        return destination_city;
    }

    public void setDestination_city(String destination_city) {
        this.destination_city = destination_city;
    }
    public String getTicket_id_() {
        return ticket_id_;
    }

    public void setTicket_id_(String ticket_id_) {
        this.ticket_id_ = ticket_id_;
    }
    public String getDate_() {
        return date_;
    }

    public void setDate_(String date_) {
        this.date_ = date_;
    }
    public String getStarting_city_() {
        return starting_city_;
    }

    public void setStarting_city_(String starting_city_) {
        this.starting_city_ = starting_city_;
    }

    public Pay getPay() {
        return pay;
    }

    public void setPay(Pay pay) {
        this.pay = pay;
    }

}