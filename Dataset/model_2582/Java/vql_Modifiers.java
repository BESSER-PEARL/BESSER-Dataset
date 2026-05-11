





import java.util.List;
import java.util.ArrayList;

public class vql_Modifiers  {

    private String execution;
    private boolean private;





    private vql_Pattern vql_pattern;


    public vql_Modifiers(
        String execution,        boolean private    ) {
        this.execution = execution;
        this.private = private;
    }


    public String getExecution() {
        return execution;
    }

    public void setExecution(String execution) {
        this.execution = execution;
    }
    public boolean getPrivate() {
        return private;
    }

    public void setPrivate(boolean private) {
        this.private = private;
    }

    public vql_Pattern getVql_pattern() {
        return vql_pattern;
    }

    public void setVql_pattern(vql_Pattern vql_pattern) {
        this.vql_pattern = vql_pattern;
    }

}