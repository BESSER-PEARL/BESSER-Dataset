





import java.util.List;
import java.util.ArrayList;

public class myDsl_Operateson  {






    private myDsl_Transaction mydsl_transaction;




    private List<myDsl_EntityName> mydsl_entitynames;


    public myDsl_Operateson(
    ) {
        this.mydsl_entitynames = new ArrayList<>();
    }

    public myDsl_Operateson(
        ArrayList<myDsl_EntityName> mydsl_entitynames    ) {
        this.mydsl_entitynames = mydsl_entitynames;
    }


    public myDsl_Transaction getMydsl_transaction() {
        return mydsl_transaction;
    }

    public void setMydsl_transaction(myDsl_Transaction mydsl_transaction) {
        this.mydsl_transaction = mydsl_transaction;
    }
    public List<myDsl_EntityName> getMydsl_entitynames() {
        return mydsl_entitynames;
    }

    public void addMydsl_entityname(Mydsl_entityname mydsl_entityname) {
        this.mydsl_entitynames.add(mydsl_entityname);
    }

}