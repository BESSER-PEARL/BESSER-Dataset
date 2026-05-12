





import java.util.List;
import java.util.ArrayList;

public class book  {

    private String Region;
    private None AuthoredBy;
    private int Year;
    private float Price;
    private None RefTo;
    private String Title;
    private None Publisher;





    private publishments publishments;


    public book(
        String Region,        None AuthoredBy,        int Year,        float Price,        None RefTo,        String Title,        None Publisher    ) {
        this.Region = Region;
        this.AuthoredBy = AuthoredBy;
        this.Year = Year;
        this.Price = Price;
        this.RefTo = RefTo;
        this.Title = Title;
        this.Publisher = Publisher;
    }


    public String getRegion() {
        return Region;
    }

    public void setRegion(String Region) {
        this.Region = Region;
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
    public float getPrice() {
        return Price;
    }

    public void setPrice(float Price) {
        this.Price = Price;
    }
    public None getRefto() {
        return RefTo;
    }

    public void setRefto(None RefTo) {
        this.RefTo = RefTo;
    }
    public String getTitle() {
        return Title;
    }

    public void setTitle(String Title) {
        this.Title = Title;
    }
    public None getPublisher() {
        return Publisher;
    }

    public void setPublisher(None Publisher) {
        this.Publisher = Publisher;
    }

    public publishments getPublishments() {
        return publishments;
    }

    public void setPublishments(publishments publishments) {
        this.publishments = publishments;
    }

}