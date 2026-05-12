





import java.util.List;
import java.util.ArrayList;

public class SWRC_Booklet extends Publication {

    private String edition;
    private String howpublished;
    private String address;
    private String month;



    public SWRC_Booklet(
        String edition,        String howpublished,        String address,        String month    ) {
        super(
        );
        this.edition = edition;
        this.howpublished = howpublished;
        this.address = address;
        this.month = month;
    }


    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getHowpublished() {
        return howpublished;
    }

    public void setHowpublished(String howpublished) {
        this.howpublished = howpublished;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }


}