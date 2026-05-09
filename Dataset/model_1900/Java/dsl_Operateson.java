





import java.util.List;
import java.util.ArrayList;

public class dsl_Operateson  {






    private dsl_Transaction dsl_transaction;




    private List<dsl_EntityName> dsl_entitynames;


    public dsl_Operateson(
    ) {
        this.dsl_entitynames = new ArrayList<>();
    }

    public dsl_Operateson(
        ArrayList<dsl_EntityName> dsl_entitynames    ) {
        this.dsl_entitynames = dsl_entitynames;
    }


    public dsl_Transaction getDsl_transaction() {
        return dsl_transaction;
    }

    public void setDsl_transaction(dsl_Transaction dsl_transaction) {
        this.dsl_transaction = dsl_transaction;
    }
    public List<dsl_EntityName> getDsl_entitynames() {
        return dsl_entitynames;
    }

    public void addDsl_entityname(Dsl_entityname dsl_entityname) {
        this.dsl_entitynames.add(dsl_entityname);
    }

}