





import java.util.List;
import java.util.ArrayList;

public class party_URL extends ContactInfo {

    private String address;



    public party_URL(
        String address    ) {
        super(
        );
        this.address = address;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }


}