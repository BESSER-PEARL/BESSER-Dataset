





import java.util.List;
import java.util.ArrayList;

public class drn_Limit  {

    private String name;
    private String value;





    private drn_Context drn_context;


    public drn_Limit(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public drn_Context getDrn_context() {
        return drn_context;
    }

    public void setDrn_context(drn_Context drn_context) {
        this.drn_context = drn_context;
    }

}