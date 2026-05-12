





import java.util.List;
import java.util.ArrayList;

public class Library_Management_System_Patron  {

    private String Magazines;
    private String SpecialStatus;
    private String OtherResources;
    private None Status;
    private String Books;



    public Library_Management_System_Patron(
        String Magazines,        String SpecialStatus,        String OtherResources,        None Status,        String Books    ) {
        this.Magazines = Magazines;
        this.SpecialStatus = SpecialStatus;
        this.OtherResources = OtherResources;
        this.Status = Status;
        this.Books = Books;
    }


    public String getMagazines() {
        return Magazines;
    }

    public void setMagazines(String Magazines) {
        this.Magazines = Magazines;
    }
    public String getSpecialstatus() {
        return SpecialStatus;
    }

    public void setSpecialstatus(String SpecialStatus) {
        this.SpecialStatus = SpecialStatus;
    }
    public String getOtherresources() {
        return OtherResources;
    }

    public void setOtherresources(String OtherResources) {
        this.OtherResources = OtherResources;
    }
    public None getStatus() {
        return Status;
    }

    public void setStatus(None Status) {
        this.Status = Status;
    }
    public String getBooks() {
        return Books;
    }

    public void setBooks(String Books) {
        this.Books = Books;
    }


}