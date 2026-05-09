




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class CodePack_DataModels_RoomBooked  {

    private LocalDate date_end;
    private LocalDate date_start;
    private int room_number;
    private int booking_id;





    private Booking booking;


    public CodePack_DataModels_RoomBooked(
        LocalDate date_end,        LocalDate date_start,        int room_number,        int booking_id    ) {
        this.date_end = date_end;
        this.date_start = date_start;
        this.room_number = room_number;
        this.booking_id = booking_id;
    }


    public LocalDate getDate_end() {
        return date_end;
    }

    public void setDate_end(LocalDate date_end) {
        this.date_end = date_end;
    }
    public LocalDate getDate_start() {
        return date_start;
    }

    public void setDate_start(LocalDate date_start) {
        this.date_start = date_start;
    }
    public int getRoom_number() {
        return room_number;
    }

    public void setRoom_number(int room_number) {
        this.room_number = room_number;
    }
    public int getBooking_id() {
        return booking_id;
    }

    public void setBooking_id(int booking_id) {
        this.booking_id = booking_id;
    }

    public Booking getBooking() {
        return booking;
    }

    public void setBooking(Booking booking) {
        this.booking = booking;
    }

}