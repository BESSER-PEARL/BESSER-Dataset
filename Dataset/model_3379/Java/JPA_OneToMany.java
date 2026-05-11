





import java.util.List;
import java.util.ArrayList;

public class JPA_OneToMany extends Anotation {

    private String fetch;
    private String cascade;



    public JPA_OneToMany(
        String fetch,        String cascade    ) {
        super(
        );
        this.fetch = fetch;
        this.cascade = cascade;
    }


    public String getFetch() {
        return fetch;
    }

    public void setFetch(String fetch) {
        this.fetch = fetch;
    }
    public String getCascade() {
        return cascade;
    }

    public void setCascade(String cascade) {
        this.cascade = cascade;
    }


}