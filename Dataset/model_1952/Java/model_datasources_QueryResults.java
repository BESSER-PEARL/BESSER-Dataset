





import java.util.List;
import java.util.ArrayList;

public class model_datasources_QueryResults  {

    private String header;
    private String id;



    public model_datasources_QueryResults(
        String header,        String id    ) {
        this.header = header;
        this.id = id;
    }


    public String getHeader() {
        return header;
    }

    public void setHeader(String header) {
        this.header = header;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}