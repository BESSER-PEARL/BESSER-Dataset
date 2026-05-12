





import java.util.List;
import java.util.ArrayList;

public class Hardware  {

    private String serialNo;
    private String manufacturer;



    public Hardware(
        String serialNo,        String manufacturer    ) {
        this.serialNo = serialNo;
        this.manufacturer = manufacturer;
    }


    public String getSerialno() {
        return serialNo;
    }

    public void setSerialno(String serialNo) {
        this.serialNo = serialNo;
    }
    public String getManufacturer() {
        return manufacturer;
    }

    public void setManufacturer(String manufacturer) {
        this.manufacturer = manufacturer;
    }


}