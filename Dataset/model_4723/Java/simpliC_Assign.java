





import java.util.List;
import java.util.ArrayList;

public class simpliC_Assign extends Stmt {

    private String var;



    public simpliC_Assign(
        String var    ) {
        super(
        );
        this.var = var;
    }


    public String getVar() {
        return var;
    }

    public void setVar(String var) {
        this.var = var;
    }


}