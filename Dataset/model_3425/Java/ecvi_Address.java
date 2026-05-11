





import java.util.List;
import java.util.ArrayList;

public class ecvi_Address  {

    private String line2;
    private String town;
    private String zIP;
    private String line1;
    private String country;
    private String state;
    private String county;





    private ecvi_GeoPoint ecvi_geopoint;




    private ecvi_Laboratory ecvi_laboratory;


    public ecvi_Address(
        String line2,        String town,        String zIP,        String line1,        String country,        String state,        String county    ) {
        this.line2 = line2;
        this.town = town;
        this.zIP = zIP;
        this.line1 = line1;
        this.country = country;
        this.state = state;
        this.county = county;
    }


    public String getLine2() {
        return line2;
    }

    public void setLine2(String line2) {
        this.line2 = line2;
    }
    public String getTown() {
        return town;
    }

    public void setTown(String town) {
        this.town = town;
    }
    public String getZip() {
        return zIP;
    }

    public void setZip(String zIP) {
        this.zIP = zIP;
    }
    public String getLine1() {
        return line1;
    }

    public void setLine1(String line1) {
        this.line1 = line1;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getState() {
        return state;
    }

    public void setState(String state) {
        this.state = state;
    }
    public String getCounty() {
        return county;
    }

    public void setCounty(String county) {
        this.county = county;
    }

    public ecvi_GeoPoint getEcvi_geopoint() {
        return ecvi_geopoint;
    }

    public void setEcvi_geopoint(ecvi_GeoPoint ecvi_geopoint) {
        this.ecvi_geopoint = ecvi_geopoint;
    }
    public ecvi_Laboratory getEcvi_laboratory() {
        return ecvi_laboratory;
    }

    public void setEcvi_laboratory(ecvi_Laboratory ecvi_laboratory) {
        this.ecvi_laboratory = ecvi_laboratory;
    }

}