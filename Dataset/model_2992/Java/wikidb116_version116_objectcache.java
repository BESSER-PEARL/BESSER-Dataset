




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class wikidb116_version116_objectcache  {

    private String value;
    private String keyname;
    private LocalDate exptime;



    public wikidb116_version116_objectcache(
        String value,        String keyname,        LocalDate exptime    ) {
        this.value = value;
        this.keyname = keyname;
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
    public LocalDate getExptime() {
        return exptime;
    }

    public void setExptime(LocalDate exptime) {
        this.exptime = exptime;
    }


}