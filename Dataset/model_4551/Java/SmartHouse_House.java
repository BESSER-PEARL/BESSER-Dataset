





import java.util.List;
import java.util.ArrayList;

public class SmartHouse_House  {

    private String outtemp;
    private String eprice;
    private String name;
    private String time;





    private SmartHouse_EV smarthouse_ev;




    private List<SmartHouse_EV> smarthouse_evs;


    public SmartHouse_House(
        String outtemp,        String eprice,        String name,        String time    ) {
        this.outtemp = outtemp;
        this.eprice = eprice;
        this.name = name;
        this.time = time;
        this.smarthouse_evs = new ArrayList<>();
    }

    public SmartHouse_House(
        String outtemp,        String eprice,        String name,        String time        ArrayList<SmartHouse_EV> smarthouse_evs    ) {
        this.outtemp = outtemp;
        this.eprice = eprice;
        this.name = name;
        this.time = time;
        this.smarthouse_evs = smarthouse_evs;
    }

    public String getOuttemp() {
        return outtemp;
    }

    public void setOuttemp(String outtemp) {
        this.outtemp = outtemp;
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
    public String getTime() {
        return time;
    }

    public void setTime(String time) {
        this.time = time;
    }

    public SmartHouse_EV getSmarthouse_ev() {
        return smarthouse_ev;
    }

    public void setSmarthouse_ev(SmartHouse_EV smarthouse_ev) {
        this.smarthouse_ev = smarthouse_ev;
    }
    public List<SmartHouse_EV> getSmarthouse_evs() {
        return smarthouse_evs;
    }

    public void addSmarthouse_ev(Smarthouse_ev smarthouse_ev) {
        this.smarthouse_evs.add(smarthouse_ev);
    }

}