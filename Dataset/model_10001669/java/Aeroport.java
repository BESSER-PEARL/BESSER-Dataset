





import java.util.List;
import java.util.ArrayList;

public class Aeroport  {

    private int altitude;
    private String nomAeroport;



    public Aeroport(
        int altitude,        String nomAeroport    ) {
        this.altitude = altitude;
        this.nomAeroport = nomAeroport;
    }


    public int getAltitude() {
        return altitude;
    }

    public void setAltitude(int altitude) {
        this.altitude = altitude;
    }
    public String getNomaeroport() {
        return nomAeroport;
    }

    public void setNomaeroport(String nomAeroport) {
        this.nomAeroport = nomAeroport;
    }


}