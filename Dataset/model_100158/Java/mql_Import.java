





import java.util.List;
import java.util.ArrayList;

public class mql_Import  {

    private String importURI;





    private mql_QueryModule mql_querymodule;


    public mql_Import(
        String importURI    ) {
        this.importURI = importURI;
    }


    public String getImporturi() {
        return importURI;
    }

    public void setImporturi(String importURI) {
        this.importURI = importURI;
    }

    public mql_QueryModule getMql_querymodule() {
        return mql_querymodule;
    }

    public void setMql_querymodule(mql_QueryModule mql_querymodule) {
        this.mql_querymodule = mql_querymodule;
    }

}