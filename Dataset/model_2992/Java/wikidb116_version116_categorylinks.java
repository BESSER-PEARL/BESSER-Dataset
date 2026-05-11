




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class wikidb116_version116_categorylinks  {

    private String cl_from;
    private LocalDate cl_timestamp;
    private String cl_to;
    private String cl_sortkey;



    public wikidb116_version116_categorylinks(
        String cl_from,        LocalDate cl_timestamp,        String cl_to,        String cl_sortkey    ) {
        this.cl_from = cl_from;
        this.cl_timestamp = cl_timestamp;
        this.cl_to = cl_to;
        this.cl_sortkey = cl_sortkey;
    }


    public String getCl_from() {
        return cl_from;
    }

    public void setCl_from(String cl_from) {
        this.cl_from = cl_from;
    }
    public LocalDate getCl_timestamp() {
        return cl_timestamp;
    }

    public void setCl_timestamp(LocalDate cl_timestamp) {
        this.cl_timestamp = cl_timestamp;
    }
    public String getCl_to() {
        return cl_to;
    }

    public void setCl_to(String cl_to) {
        this.cl_to = cl_to;
    }
    public String getCl_sortkey() {
        return cl_sortkey;
    }

    public void setCl_sortkey(String cl_sortkey) {
        this.cl_sortkey = cl_sortkey;
    }


}