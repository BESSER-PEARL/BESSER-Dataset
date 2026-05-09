





import java.util.List;
import java.util.ArrayList;

public class model_datasources_DataSource extends Node {

    private String dataSourceService;
    private String url;





    private Query query;




    private List<Query> querys;


    public model_datasources_DataSource(
        String dataSourceService,        String url    ) {
        super(
        );
        this.dataSourceService = dataSourceService;
        this.url = url;
        this.querys = new ArrayList<>();
    }

    public model_datasources_DataSource(
        String dataSourceService,        String url        ArrayList<Query> querys    ) {
        this.dataSourceService = dataSourceService;
        this.url = url;
        this.querys = querys;
    }

    public String getDatasourceservice() {
        return dataSourceService;
    }

    public void setDatasourceservice(String dataSourceService) {
        this.dataSourceService = dataSourceService;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public Query getQuery() {
        return query;
    }

    public void setQuery(Query query) {
        this.query = query;
    }
    public List<Query> getQuerys() {
        return querys;
    }

    public void addQuery(Query query) {
        this.querys.add(query);
    }

}