





import java.util.List;
import java.util.ArrayList;

public class libsys_User  {






    private libsys_BorrowedEntry libsys_borrowedentry;




    private libsys_ReservationEntry libsys_reservationentry;


    public libsys_User(
    ) {
    }



    public libsys_BorrowedEntry getLibsys_borrowedentry() {
        return libsys_borrowedentry;
    }

    public void setLibsys_borrowedentry(libsys_BorrowedEntry libsys_borrowedentry) {
        this.libsys_borrowedentry = libsys_borrowedentry;
    }
    public libsys_ReservationEntry getLibsys_reservationentry() {
        return libsys_reservationentry;
    }

    public void setLibsys_reservationentry(libsys_ReservationEntry libsys_reservationentry) {
        this.libsys_reservationentry = libsys_reservationentry;
    }

}