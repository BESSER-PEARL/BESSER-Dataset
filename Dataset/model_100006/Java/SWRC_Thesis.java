





import java.util.List;
import java.util.ArrayList;

public class SWRC_Thesis extends Publication {

    private String type;
    private String month;
    private String address;



    public SWRC_Thesis(
        String type,        String month,        String address    ) {
        super(
        );
        this.type = type;
        this.month = month;
        this.address = address;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
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