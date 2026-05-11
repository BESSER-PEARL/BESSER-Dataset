





import java.util.List;
import java.util.ArrayList;

public class mongoQuery_QueryObject extends Query {






    private List<mongoQuery_Query> mongoquery_querys;


    public mongoQuery_QueryObject(
    ) {
        super(
        );
        this.mongoquery_querys = new ArrayList<>();
    }

    public mongoQuery_QueryObject(
        ArrayList<mongoQuery_Query> mongoquery_querys    ) {
        this.mongoquery_querys = mongoquery_querys;
    }


    public List<mongoQuery_Query> getMongoquery_querys() {
        return mongoquery_querys;
    }

    public void addMongoquery_query(Mongoquery_query mongoquery_query) {
        this.mongoquery_querys.add(mongoquery_query);
    }

}