





import java.util.List;
import java.util.ArrayList;

public class apromore_Edge  {

    private int ident;
    private boolean default;
    private String condition;



    public apromore_Edge(
        int ident,        boolean default,        String condition    ) {
        this.ident = ident;
        this.default = default;
        this.condition = condition;
    }


    public int getIdent() {
        return ident;
    }

    public void setIdent(int ident) {
        this.ident = ident;
    }
    public boolean getDefault() {
        return default;
    }

    public void setDefault(boolean default) {
        this.default = default;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }


}