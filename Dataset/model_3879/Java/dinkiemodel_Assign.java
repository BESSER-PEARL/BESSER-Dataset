





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_Assign extends Statement {

    private String varName;



    public dinkiemodel_Assign(
        String varName    ) {
        super(
        );
        this.varName = varName;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }


}