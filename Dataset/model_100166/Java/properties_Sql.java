





import java.util.List;
import java.util.ArrayList;

public class properties_Sql  {

    private String id;
    private String hqlQuery;



    public properties_Sql(
        String id,        String hqlQuery    ) {
        this.id = id;
        this.hqlQuery = hqlQuery;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getHqlquery() {
        return hqlQuery;
    }

    public void setHqlquery(String hqlQuery) {
        this.hqlQuery = hqlQuery;
    }


}