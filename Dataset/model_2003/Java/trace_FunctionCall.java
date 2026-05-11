





import java.util.List;
import java.util.ArrayList;

public class trace_FunctionCall extends Step {

    private String displayName;
    private String id;



    public trace_FunctionCall(
        String displayName,        String id    ) {
        super(
        );
        this.displayName = displayName;
        this.id = id;
    }


    public String getDisplayname() {
        return displayName;
    }

    public void setDisplayname(String displayName) {
        this.displayName = displayName;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }


}