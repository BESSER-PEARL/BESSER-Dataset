





import java.util.List;
import java.util.ArrayList;

public class Hall  {

    private String cost_per_day;
    private String get_hall_no;
    private String get_room_type;



    public Hall(
        String cost_per_day,        String get_hall_no,        String get_room_type    ) {
        this.cost_per_day = cost_per_day;
        this.get_hall_no = get_hall_no;
        this.get_room_type = get_room_type;
    }


    public String getCost_per_day() {
        return cost_per_day;
    }

    public void setCost_per_day(String cost_per_day) {
        this.cost_per_day = cost_per_day;
    }
    public String getGet_hall_no() {
        return get_hall_no;
    }

    public void setGet_hall_no(String get_hall_no) {
        this.get_hall_no = get_hall_no;
    }
    public String getGet_room_type() {
        return get_room_type;
    }

    public void setGet_room_type(String get_room_type) {
        this.get_room_type = get_room_type;
    }


}