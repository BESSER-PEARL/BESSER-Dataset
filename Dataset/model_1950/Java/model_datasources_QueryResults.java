





import java.util.List;
import java.util.ArrayList;

public class model_datasources_QueryResults  {

    private String header;
    private String id;





    private List<AQueryResult> aqueryresults;


    public model_datasources_QueryResults(
        String header,        String id    ) {
        this.header = header;
        this.id = id;
        this.aqueryresults = new ArrayList<>();
    }

    public model_datasources_QueryResults(
        String header,        String id        ArrayList<AQueryResult> aqueryresults    ) {
        this.header = header;
        this.id = id;
        this.aqueryresults = aqueryresults;
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

    public List<AQueryResult> getAqueryresults() {
        return aqueryresults;
    }

    public void addAqueryresult(Aqueryresult aqueryresult) {
        this.aqueryresults.add(aqueryresult);
    }

}