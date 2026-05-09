





import java.util.List;
import java.util.ArrayList;

public class eTJ_Booking  {

    private int overtime;
    private int sloppy;





    private eTJ_BookingResource etj_bookingresource;




    private eTJ_BookingTask etj_bookingtask;


    public eTJ_Booking(
        int overtime,        int sloppy    ) {
        this.overtime = overtime;
        this.sloppy = sloppy;
    }


    public int getOvertime() {
        return overtime;
    }

    public void setOvertime(int overtime) {
        this.overtime = overtime;
    }
    public int getSloppy() {
        return sloppy;
    }

    public void setSloppy(int sloppy) {
        this.sloppy = sloppy;
    }

    public eTJ_BookingResource getEtj_bookingresource() {
        return etj_bookingresource;
    }

    public void setEtj_bookingresource(eTJ_BookingResource etj_bookingresource) {
        this.etj_bookingresource = etj_bookingresource;
    }
    public eTJ_BookingTask getEtj_bookingtask() {
        return etj_bookingtask;
    }

    public void setEtj_bookingtask(eTJ_BookingTask etj_bookingtask) {
        this.etj_bookingtask = etj_bookingtask;
    }

}