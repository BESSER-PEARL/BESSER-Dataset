




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class libsys_BorrowedEntry  {

    private LocalDate returnDate;





    private libsys_Instance libsys_instance;


    public libsys_BorrowedEntry(
        LocalDate returnDate    ) {
        this.returnDate = returnDate;
    }


    public LocalDate getReturndate() {
        return returnDate;
    }

    public void setReturndate(LocalDate returnDate) {
        this.returnDate = returnDate;
    }

    public libsys_Instance getLibsys_instance() {
        return libsys_instance;
    }

    public void setLibsys_instance(libsys_Instance libsys_instance) {
        this.libsys_instance = libsys_instance;
    }

}