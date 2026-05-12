





import java.util.List;
import java.util.ArrayList;

public class properties_SqlQuery extends Sql {

    private String queryString;





    private properties_SpecificDBMSProperties properties_specificdbmsproperties;


    public properties_SqlQuery(
        String queryString    ) {
        super(
        );
        this.queryString = queryString;
    }


    public String getQuerystring() {
        return queryString;
    }

    public void setQuerystring(String queryString) {
        this.queryString = queryString;
    }

    public properties_SpecificDBMSProperties getProperties_specificdbmsproperties() {
        return properties_specificdbmsproperties;
    }

    public void setProperties_specificdbmsproperties(properties_SpecificDBMSProperties properties_specificdbmsproperties) {
        this.properties_specificdbmsproperties = properties_specificdbmsproperties;
    }

}