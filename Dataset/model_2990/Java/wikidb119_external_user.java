





import java.util.List;
import java.util.ArrayList;

public class wikidb119_external_user  {

    private String eu_external_id;
    private String eu_local_id;



    public wikidb119_external_user(
        String eu_external_id,        String eu_local_id    ) {
        this.eu_external_id = eu_external_id;
        this.eu_local_id = eu_local_id;
    }


    public String getEu_external_id() {
        return eu_external_id;
    }

    public void setEu_external_id(String eu_external_id) {
        this.eu_external_id = eu_external_id;
    }
    public String getEu_local_id() {
        return eu_local_id;
    }

    public void setEu_local_id(String eu_local_id) {
        this.eu_local_id = eu_local_id;
    }


}