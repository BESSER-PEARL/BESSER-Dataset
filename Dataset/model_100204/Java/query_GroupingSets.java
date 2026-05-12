





import java.util.List;
import java.util.ArrayList;

public class query_GroupingSets extends GroupingSpecification {






    private query_GroupingSetsElement query_groupingsetselement;




    private List<query_GroupingSetsElement> query_groupingsetselements;


    public query_GroupingSets(
    ) {
        super(
        );
        this.query_groupingsetselements = new ArrayList<>();
    }

    public query_GroupingSets(
        ArrayList<query_GroupingSetsElement> query_groupingsetselements    ) {
        this.query_groupingsetselements = query_groupingsetselements;
    }


    public query_GroupingSetsElement getQuery_groupingsetselement() {
        return query_groupingsetselement;
    }

    public void setQuery_groupingsetselement(query_GroupingSetsElement query_groupingsetselement) {
        this.query_groupingsetselement = query_groupingsetselement;
    }
    public List<query_GroupingSetsElement> getQuery_groupingsetselements() {
        return query_groupingsetselements;
    }

    public void addQuery_groupingsetselement(Query_groupingsetselement query_groupingsetselement) {
        this.query_groupingsetselements.add(query_groupingsetselement);
    }

}