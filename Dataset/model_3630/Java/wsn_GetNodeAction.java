





import java.util.List;
import java.util.ArrayList;

public class wsn_GetNodeAction extends Action,  {

    private String query;



    public wsn_GetNodeAction(
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