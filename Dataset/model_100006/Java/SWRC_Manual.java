





import java.util.List;
import java.util.ArrayList;

public class SWRC_Manual extends Publication {

    private String edition;
    private String month;
    private String address;



    public SWRC_Manual(
        String edition,        String month,        String address    ) {
        super(
        );
        this.edition = edition;
        this.month = month;
        this.address = address;
    }


    public String getEdition() {
        return edition;
    }

    public void setEdition(String edition) {
        this.edition = edition;
    }
    public String getMonth() {
        return month;
    }

    public void setMonth(String month) {
        this.month = month;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}