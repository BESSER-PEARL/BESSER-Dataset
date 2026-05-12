





import java.util.List;
import java.util.ArrayList;

public class plSql_DeclareSection  {






    private plSql_ProcedureImplementation plsql_procedureimplementation;




    private List<plSql_Item> plsql_items;


    public plSql_DeclareSection(
    ) {
        this.plsql_items = new ArrayList<>();
    }

    public plSql_DeclareSection(
        ArrayList<plSql_Item> plsql_items    ) {
        this.plsql_items = plsql_items;
    }


    public plSql_ProcedureImplementation getPlsql_procedureimplementation() {
        return plsql_procedureimplementation;
    }

    public void setPlsql_procedureimplementation(plSql_ProcedureImplementation plsql_procedureimplementation) {
        this.plsql_procedureimplementation = plsql_procedureimplementation;
    }
    public List<plSql_Item> getPlsql_items() {
        return plsql_items;
    }

    public void addPlsql_item(Plsql_item plsql_item) {
        this.plsql_items.add(plsql_item);
    }

}