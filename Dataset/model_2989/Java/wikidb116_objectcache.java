




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class wikidb116_objectcache  {

    private String value;
    private LocalDate exptime;
    private String keyname;



    public wikidb116_objectcache(
        String value,        LocalDate exptime,        String keyname    ) {
        this.value = value;
        this.exptime = exptime;
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
    public String getKeyname() {
        return keyname;
    }

    public void setKeyname(String keyname) {
        this.keyname = keyname;
    }


}