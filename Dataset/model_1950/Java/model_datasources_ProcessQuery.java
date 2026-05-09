





import java.util.List;
import java.util.ArrayList;

public class model_datasources_ProcessQuery extends Query {

    private String queryProcessorId;



    public model_datasources_ProcessQuery(
        String queryProcessorId    ) {
        super(
        );
        this.queryProcessorId = queryProcessorId;
    }


    public String getQueryprocessorid() {
        return queryProcessorId;
    }

    public void setQueryprocessorid(String queryProcessorId) {
        this.queryProcessorId = queryProcessorId;
    }


}