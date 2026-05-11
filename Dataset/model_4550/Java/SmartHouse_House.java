





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_House  {

    private String eprice;
    private String name;
    private String outtemp;
    private String time;



    public SmartHouse_House(
        String eprice,        String name,        String outtemp,        String time    ) {
        this.eprice = eprice;
        this.name = name;
        this.outtemp = outtemp;
        this.time = time;
    }


    public String getEprice() {
        return eprice;
    }

    public void setEprice(String eprice) {
        this.eprice = eprice;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getOuttemp() {
        return outtemp;
    }

    public void setOuttemp(String outtemp) {
        this.outtemp = outtemp;
    }
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }


}