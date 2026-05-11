




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class wikidb119_categorylinks  {

    private LocalDate cl_timestamp;
    private String cl_sortkey_prefix;
    private String cl_to;
    private String cl_from;
    private String cl_sortkey;
    private String cl_type;
    private String cl_collation;



    public wikidb119_categorylinks(
        LocalDate cl_timestamp,        String cl_sortkey_prefix,        String cl_to,        String cl_from,        String cl_sortkey,        String cl_type,        String cl_collation    ) {
        this.cl_timestamp = cl_timestamp;
        this.cl_sortkey_prefix = cl_sortkey_prefix;
        this.cl_to = cl_to;
        this.cl_from = cl_from;
        this.cl_sortkey = cl_sortkey;
        this.cl_type = cl_type;
        this.cl_collation = cl_collation;
    }


    public LocalDate getCl_timestamp() {
        return cl_timestamp;
    }

    public void setCl_timestamp(LocalDate cl_timestamp) {
        this.cl_timestamp = cl_timestamp;
    }
    public String getCl_sortkey_prefix() {
        return cl_sortkey_prefix;
    }

    public void setCl_sortkey_prefix(String cl_sortkey_prefix) {
        this.cl_sortkey_prefix = cl_sortkey_prefix;
    }
    public String getCl_to() {
        return cl_to;
    }

    public void setCl_to(String cl_to) {
        this.cl_to = cl_to;
    }
    public String getCl_from() {
        return cl_from;
    }

    public void setCl_from(String cl_from) {
        this.cl_from = cl_from;
    }
    public String getCl_sortkey() {
        return cl_sortkey;
    }

    public void setCl_sortkey(String cl_sortkey) {
        this.cl_sortkey = cl_sortkey;
    }
    public String getCl_type() {
        return cl_type;
    }

    public void setCl_type(String cl_type) {
        this.cl_type = cl_type;
    }
    public String getCl_collation() {
        return cl_collation;
    }

    public void setCl_collation(String cl_collation) {
        this.cl_collation = cl_collation;
    }


}