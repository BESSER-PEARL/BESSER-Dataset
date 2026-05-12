





import java.util.List;
import java.util.ArrayList;

public class Library_Management_System_Patron  {

    private String Books;
    private String SpecialStatus;
    private None Status;
    private String OtherResources;
    private String Magazines;



    public Library_Management_System_Patron(
        String Books,        String SpecialStatus,        None Status,        String OtherResources,        String Magazines    ) {
        this.Books = Books;
        this.SpecialStatus = SpecialStatus;
        this.Status = Status;
        this.OtherResources = OtherResources;
        this.Magazines = Magazines;
    }


    public String getBooks() {
        return Books;
    }

    public void setBooks(String Books) {
        this.Books = Books;
    }
    public String getSpecialstatus() {
        return SpecialStatus;
    }

    public void setSpecialstatus(String SpecialStatus) {
        this.SpecialStatus = SpecialStatus;
    }
    public None getStatus() {
        return Status;
    }

    public void setStatus(None Status) {
        this.Status = Status;
    }
    public String getOtherresources() {
        return OtherResources;
    }

    public void setOtherresources(String OtherResources) {
        this.OtherResources = OtherResources;
    }
    public String getMagazines() {
        return Magazines;
    }

    public void setMagazines(String Magazines) {
        this.Magazines = Magazines;
    }


}