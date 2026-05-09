





import java.util.List;
import java.util.ArrayList;

public class se_hotelsystem_Booking  {

    private boolean confirmed;
    private String endDate;
    private String startDate;
    private int bookingId;
    private boolean canceled;



    public se_hotelsystem_Booking(
        boolean confirmed,        String endDate,        String startDate,        int bookingId,        boolean canceled    ) {
        this.confirmed = confirmed;
        this.endDate = endDate;
        this.startDate = startDate;
        this.bookingId = bookingId;
        this.canceled = canceled;
    }


    public boolean getConfirmed() {
        return confirmed;
    }

    public void setConfirmed(boolean confirmed) {
        this.confirmed = confirmed;
    }
    public String getEnddate() {
        return endDate;
    }

    public void setEnddate(String endDate) {
        this.endDate = endDate;
    }
    public String getStartdate() {
        return startDate;
    }

    public void setStartdate(String startDate) {
        this.startDate = startDate;
    }
    public int getBookingid() {
        return bookingId;
    }

    public void setBookingid(int bookingId) {
        this.bookingId = bookingId;
    }
    public boolean getCanceled() {
        return canceled;
    }

    public void setCanceled(boolean canceled) {
        this.canceled = canceled;
    }


}