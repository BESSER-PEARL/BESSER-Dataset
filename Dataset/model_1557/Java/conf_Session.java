





import java.util.List;
import java.util.ArrayList;

public class conf_Session  {

    private String year;





    private conf_Conference conf_conference;


    public conf_Session(
        String year    ) {
        this.year = year;
    }


    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public conf_Conference getConf_conference() {
        return conf_conference;
    }

    public void setConf_conference(conf_Conference conf_conference) {
        this.conf_conference = conf_conference;
    }

}