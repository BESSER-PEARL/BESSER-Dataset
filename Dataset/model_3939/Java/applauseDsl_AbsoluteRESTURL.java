





import java.util.List;
import java.util.ArrayList;

public class applauseDsl_AbsoluteRESTURL extends RESTURL {

    private int port;





    private applauseDsl_DataSource applausedsl_datasource;


    public applauseDsl_AbsoluteRESTURL(
        int port    ) {
        super(
        );
        this.port = port;
    }


    public int getPort() {
        return port;
    }

    public void setPort(int port) {
        this.port = port;
    }

    public applauseDsl_DataSource getApplausedsl_datasource() {
        return applausedsl_datasource;
    }

    public void setApplausedsl_datasource(applauseDsl_DataSource applausedsl_datasource) {
        this.applausedsl_datasource = applausedsl_datasource;
    }

}