





import java.util.List;
import java.util.ArrayList;

public class conf101_Session extends NamedElement {

    private String year;





    private conf101_Conference conf101_conference;


    public conf101_Session(
        String year    ) {
        super(
        );
        this.year = year;
    }


    public String getYear() {
        return year;
    }

    public void setYear(String year) {
        this.year = year;
    }

    public conf101_Conference getConf101_conference() {
        return conf101_conference;
    }

    public void setConf101_conference(conf101_Conference conf101_conference) {
        this.conf101_conference = conf101_conference;
    }

}