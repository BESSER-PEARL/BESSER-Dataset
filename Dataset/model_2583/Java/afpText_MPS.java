





import java.util.List;
import java.util.ArrayList;

public class afpText_MPS extends structuredField {

    private String Reserved;
    private String RGLength;



    public afpText_MPS(
        String Reserved,        String RGLength    ) {
        super(
        );
        this.Reserved = Reserved;
        this.RGLength = RGLength;
    }


    public String getReserved() {
        return Reserved;
    }

    public void setReserved(String Reserved) {
        this.Reserved = Reserved;
    }
    public String getRglength() {
        return RGLength;
    }

    public void setRglength(String RGLength) {
        this.RGLength = RGLength;
    }


}