





import java.util.List;
import java.util.ArrayList;

public class database_View extends AbstractTable {

    private String query;



    public database_View(
        String query    ) {
        super(
        );
        this.query = query;
    }


    public String getQuery() {
        return query;
    }

    public void setQuery(String query) {
        this.query = query;
    }


}