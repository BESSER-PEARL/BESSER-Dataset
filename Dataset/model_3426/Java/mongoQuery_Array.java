





import java.util.List;
import java.util.ArrayList;

public class mongoQuery_Array  {






    private mongoQuery_Query mongoquery_query;




    private List<mongoQuery_Query> mongoquery_querys;


    public mongoQuery_Array(
    ) {
        this.mongoquery_querys = new ArrayList<>();
    }

    public mongoQuery_Array(
        ArrayList<mongoQuery_Query> mongoquery_querys    ) {
        this.mongoquery_querys = mongoquery_querys;
    }


    public mongoQuery_Query getMongoquery_query() {
        return mongoquery_query;
    }

    public void setMongoquery_query(mongoQuery_Query mongoquery_query) {
        this.mongoquery_query = mongoquery_query;
    }
    public List<mongoQuery_Query> getMongoquery_querys() {
        return mongoquery_querys;
    }

    public void addMongoquery_query(Mongoquery_query mongoquery_query) {
        this.mongoquery_querys.add(mongoquery_query);
    }

}