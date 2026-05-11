





import java.util.List;
import java.util.ArrayList;

public class relational_obeo_Database extends ModelElement {

    private String name;
    private String url;



    public relational_obeo_Database(
        String name,        String url    ) {
        super(
        );
        this.name = name;
        this.url = url;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }


}