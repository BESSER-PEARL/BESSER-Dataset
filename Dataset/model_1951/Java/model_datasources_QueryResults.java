





import java.util.List;
import java.util.ArrayList;

public class model_datasources_QueryResults  {

    private String id;
    private String header;



    public model_datasources_QueryResults(
        String id,        String header    ) {
        this.id = id;
        this.header = header;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getHeader() {
        return header;
    }

    public void setHeader(String header) {
        this.header = header;
    }


}