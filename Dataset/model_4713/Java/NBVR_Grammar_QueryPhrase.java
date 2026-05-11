





import java.util.List;
import java.util.ArrayList;

public class NBVR_Grammar_QueryPhrase extends RolePhrase {

    private String query;



    public NBVR_Grammar_QueryPhrase(
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