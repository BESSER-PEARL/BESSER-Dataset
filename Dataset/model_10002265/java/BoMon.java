





import java.util.List;
import java.util.ArrayList;

public class BoMon  {

    private String mabomon;
    private String tenbomon;



    public BoMon(
        String mabomon,        String tenbomon    ) {
        this.mabomon = mabomon;
        this.tenbomon = tenbomon;
    }


    public String getMabomon() {
        return mabomon;
    }

    public void setMabomon(String mabomon) {
        this.mabomon = mabomon;
    }
    public String getTenbomon() {
        return tenbomon;
    }

    public void setTenbomon(String tenbomon) {
        this.tenbomon = tenbomon;
    }


}