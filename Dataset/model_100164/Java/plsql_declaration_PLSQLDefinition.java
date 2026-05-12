





import java.util.List;
import java.util.ArrayList;

public class plsql_declaration_PLSQLDefinition  {






    private List<TriggerBlock> triggerblocks;


    public plsql_declaration_PLSQLDefinition(
    ) {
        this.triggerblocks = new ArrayList<>();
    }

    public plsql_declaration_PLSQLDefinition(
        ArrayList<TriggerBlock> triggerblocks    ) {
        this.triggerblocks = triggerblocks;
    }


    public List<TriggerBlock> getTriggerblocks() {
        return triggerblocks;
    }

    public void addTriggerblock(Triggerblock triggerblock) {
        this.triggerblocks.add(triggerblock);
    }

}