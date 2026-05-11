





import java.util.List;
import java.util.ArrayList;

public class conversation_State  {

    private boolean join;
    private String name;
    private boolean requiresExecution;



    public conversation_State(
        boolean join,        String name,        boolean requiresExecution    ) {
        this.join = join;
        this.name = name;
        this.requiresExecution = requiresExecution;
    }


    public boolean getJoin() {
        return join;
    }

    public void setJoin(boolean join) {
        this.join = join;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public boolean getRequiresexecution() {
        return requiresExecution;
    }

    public void setRequiresexecution(boolean requiresExecution) {
        this.requiresExecution = requiresExecution;
    }


}