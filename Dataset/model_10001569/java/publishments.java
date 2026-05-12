





import java.util.List;
import java.util.ArrayList;

public class publishments  {

    private int Year;
    private None Publisher;
    private None AuthoredBy;
    private String Title;



    public publishments(
        int Year,        None Publisher,        None AuthoredBy,        String Title    ) {
        this.Year = Year;
        this.Publisher = Publisher;
        this.AuthoredBy = AuthoredBy;
        this.Title = Title;
    }


    public int getYear() {
        return Year;
    }

    public void setYear(int Year) {
        this.Year = Year;
    }
    public None getPublisher() {
        return Publisher;
    }

    public void setPublisher(None Publisher) {
        this.Publisher = Publisher;
    }
    public None getAuthoredby() {
        return AuthoredBy;
    }

    public void setAuthoredby(None AuthoredBy) {
        this.AuthoredBy = AuthoredBy;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }


}