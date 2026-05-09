




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_ExtraService  {

    private String type;
    private LocalDate date_start;
    private int booking_id;
    private float total_price;
    private LocalDate date_end;



    public CodePack_DataModels_ExtraService(
        String type,        LocalDate date_start,        int booking_id,        float total_price,        LocalDate date_end    ) {
        this.type = type;
        this.date_start = date_start;
        this.booking_id = booking_id;
        this.total_price = total_price;
        this.date_end = date_end;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public LocalDate getDate_start() {
        return date_start;
    }

    public void setDate_start(LocalDate date_start) {
        this.date_start = date_start;
    }
    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
    }
    public float getTotal_price() {
        return total_price;
    }

    public void setTotal_price(float total_price) {
        this.total_price = total_price;
    }
    public LocalDate getDate_end() {
        return date_end;
    }

    public void setDate_end(LocalDate date_end) {
        this.date_end = date_end;
    }


}