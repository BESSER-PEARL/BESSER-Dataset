





import java.util.List;
import java.util.ArrayList;

public class JPA_OneToMany extends Anotation {

    private String cascade;
    private String fetch;



    public JPA_OneToMany(
        String cascade,        String fetch    ) {
        super(
        );
        this.cascade = cascade;
        this.fetch = fetch;
    }


    public String getCascade() {
        return cascade;
    }

    public void setCascade(String cascade) {
        this.cascade = cascade;
    }
    public String getFetch() {
        return fetch;
    }

    public void setFetch(String fetch) {
        this.fetch = fetch;
    }


}