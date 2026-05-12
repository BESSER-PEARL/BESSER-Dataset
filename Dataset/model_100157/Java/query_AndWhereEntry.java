





import java.util.List;
import java.util.ArrayList;

public class query_AndWhereEntry extends WhereEntry {






    private List<query_WhereEntry> query_whereentrys;


    public query_AndWhereEntry(
    ) {
        super(
        );
        this.query_whereentrys = new ArrayList<>();
    }

    public query_AndWhereEntry(
        ArrayList<query_WhereEntry> query_whereentrys    ) {
        this.query_whereentrys = query_whereentrys;
    }


    public List<query_WhereEntry> getQuery_whereentrys() {
        return query_whereentrys;
    }

    public void addQuery_whereentry(Query_whereentry query_whereentry) {
        this.query_whereentrys.add(query_whereentry);
    }

}