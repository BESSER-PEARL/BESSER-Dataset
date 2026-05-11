




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class wikidb119_objectcache  {

    private LocalDate exptime;
    private String value;
    private String keyname;



    public wikidb119_objectcache(
        LocalDate exptime,        String value,        String keyname    ) {
        this.exptime = exptime;
        this.value = value;
        this.keyname = keyname;
    }


    public LocalDate getExptime() {
        return exptime;
    }

    public void setExptime(LocalDate exptime) {
        this.exptime = exptime;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getKeyname() {
        return keyname;
    }

    public void setKeyname(String keyname) {
        this.keyname = keyname;
    }


}