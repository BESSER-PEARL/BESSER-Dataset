





import java.util.List;
import java.util.ArrayList;

public class model_datasources_DataSource extends Node {

    private String dataSourceService;
    private String url;



    public model_datasources_DataSource(
        String dataSourceService,        String url    ) {
        super(
        );
        this.dataSourceService = dataSourceService;
        this.url = url;
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


}