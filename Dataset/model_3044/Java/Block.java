





import java.util.List;
import java.util.ArrayList;

public class Block  {






    private behavioral_actions_Statement behavioral_actions_statement;




    private behavioral_actions_StatementWithNestedBlocks behavioral_actions_statementwithnestedblocks;


    public Block(
    ) {
    }



    public behavioral_actions_Statement getBehavioral_actions_statement() {
        return behavioral_actions_statement;
    }

    public void setBehavioral_actions_statement(behavioral_actions_Statement behavioral_actions_statement) {
        this.behavioral_actions_statement = behavioral_actions_statement;
    }
    public behavioral_actions_StatementWithNestedBlocks getBehavioral_actions_statementwithnestedblocks() {
        return behavioral_actions_statementwithnestedblocks;
    }

    public void setBehavioral_actions_statementwithnestedblocks(behavioral_actions_StatementWithNestedBlocks behavioral_actions_statementwithnestedblocks) {
        this.behavioral_actions_statementwithnestedblocks = behavioral_actions_statementwithnestedblocks;
    }

}