




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class wikidb119_objectcache  {

    private String keyname;
    private String value;
    private LocalDate exptime;



    public wikidb119_objectcache(
        String keyname,        String value,        LocalDate exptime    ) {
        this.keyname = keyname;
        this.value = value;
        this.exptime = exptime;
    }


    public String getKeyname() {
        return keyname;
    }

    public void setKeyname(String keyname) {
        this.keyname = keyname;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public LocalDate getExptime() {
        return exptime;
    }

    public void setExptime(LocalDate exptime) {
        this.exptime = exptime;
    }


}