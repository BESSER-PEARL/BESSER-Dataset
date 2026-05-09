




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class libsys_Instance  {

    private String status;
    private String rentalPeriod;
    private LocalDate returnDate;
    private String comments;
    private String shelfmark;
    private String location;
    private String components;





    private libsys_Medium libsys_medium;


    public libsys_Instance(
        String status,        String rentalPeriod,        LocalDate returnDate,        String comments,        String shelfmark,        String location,        String components    ) {
        this.status = status;
        this.rentalPeriod = rentalPeriod;
        this.returnDate = returnDate;
        this.comments = comments;
        this.shelfmark = shelfmark;
        this.location = location;
        this.components = components;
    }


    public String getStatus() {
        return status;
    }

    public void setStatus(String status) {
        this.status = status;
    }
    public String getRentalperiod() {
        return rentalPeriod;
    }

    public void setRentalperiod(String rentalPeriod) {
        this.rentalPeriod = rentalPeriod;
    }
    public LocalDate getReturndate() {
        return returnDate;
    }

    public void setReturndate(LocalDate returnDate) {
        this.returnDate = returnDate;
    }
    public String getComments() {
        return comments;
    }

    public void setComments(String comments) {
        this.comments = comments;
    }
    public String getShelfmark() {
        return shelfmark;
    }

    public void setShelfmark(String shelfmark) {
        this.shelfmark = shelfmark;
    }
    public String getLocation() {
        return location;
    }

    public void setLocation(String location) {
        this.location = location;
    }
    public String getComponents() {
        return components;
    }

    public void setComponents(String components) {
        this.components = components;
    }

    public libsys_Medium getLibsys_medium() {
        return libsys_medium;
    }

    public void setLibsys_medium(libsys_Medium libsys_medium) {
        this.libsys_medium = libsys_medium;
    }

}