





import java.util.List;
import java.util.ArrayList;

public class jpql_Import  {

    private String importURI;





    private jpql_QueryModule jpql_querymodule;


    public jpql_Import(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public jpql_QueryModule getJpql_querymodule() {
        return jpql_querymodule;
    }

    public void setJpql_querymodule(jpql_QueryModule jpql_querymodule) {
        this.jpql_querymodule = jpql_querymodule;
    }

}