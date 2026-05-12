





import java.util.List;
import java.util.ArrayList;

public class conference_paper  {

    private String Title;
    private String ConferenceName;
    private None AuthoredBy;
    private int Year;
    private None Publisher;
    private String Location;





    private publishments publishments;


    public conference_paper(
        String Title,        String ConferenceName,        None AuthoredBy,        int Year,        None Publisher,        String Location    ) {
        this.Title = Title;
        this.ConferenceName = ConferenceName;
        this.AuthoredBy = AuthoredBy;
        this.Year = Year;
        this.Publisher = Publisher;
        this.Location = Location;
    }


    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public String getConferencename() {
        return ConferenceName;
    }

    public void setConferencename(String ConferenceName) {
        this.ConferenceName = ConferenceName;
    }
    public None getAuthoredby() {
        return AuthoredBy;
    }

    public void setAuthoredby(None AuthoredBy) {
        this.AuthoredBy = AuthoredBy;
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
    public String getLocation() {
        return Location;
    }

    public void setLocation(String Location) {
        this.Location = Location;
    }

    public publishments getPublishments() {
        return publishments;
    }

    public void setPublishments(publishments publishments) {
        this.publishments = publishments;
    }

}