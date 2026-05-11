





import java.util.List;
import java.util.ArrayList;

public class wsn_GetDataAction extends Action,  {

    private String query;



    public wsn_GetDataAction(
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