





import java.util.List;
import java.util.ArrayList;

public class mql_NamedQuery  {

    private String name;





    private mql_QueryModule mql_querymodule;




    private mql_MQuery mql_mquery;


    public mql_NamedQuery(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mql_QueryModule getMql_querymodule() {
        return mql_querymodule;
    }

    public void setMql_querymodule(mql_QueryModule mql_querymodule) {
        this.mql_querymodule = mql_querymodule;
    }
    public mql_MQuery getMql_mquery() {
        return mql_mquery;
    }

    public void setMql_mquery(mql_MQuery mql_mquery) {
        this.mql_mquery = mql_mquery;
    }

}