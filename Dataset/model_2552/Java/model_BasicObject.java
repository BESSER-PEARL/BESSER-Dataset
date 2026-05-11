





import java.util.List;
import java.util.ArrayList;

public class model_BasicObject  {

    private String id;
    private String locale;
    private int domain;



    public model_BasicObject(
        String id,        String locale,        int domain    ) {
        this.id = id;
        this.locale = locale;
        this.domain = domain;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getLocale() {
        return locale;
    }

    public void setLocale(String locale) {
        this.locale = locale;
    }
    public int getDomain() {
        return domain;
    }

    public void setDomain(int domain) {
        this.domain = domain;
    }


}