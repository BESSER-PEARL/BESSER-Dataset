





import java.util.List;
import java.util.ArrayList;

public class Osiguranje  {

    private String OsigurKuca;
    private int OsiguranjeID;



    public Osiguranje(
        String OsigurKuca,        int OsiguranjeID    ) {
        this.OsigurKuca = OsigurKuca;
        this.OsiguranjeID = OsiguranjeID;
    }


    public String getOsigurkuca() {
        return OsigurKuca;
    }

    public void setOsigurkuca(String OsigurKuca) {
        this.OsigurKuca = OsigurKuca;
    }
    public int getOsiguranjeid() {
        return OsiguranjeID;
    }

    public void setOsiguranjeid(int OsiguranjeID) {
        this.OsiguranjeID = OsiguranjeID;
    }


}