





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_Declaration extends Statement {

    private String varName;
    private boolean global_;



    public dinkiemodel_Declaration(
        String varName,        boolean global_    ) {
        super(
        );
        this.varName = varName;
        this.global_ = global_;
    }


    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }
    public boolean getGlobal_() {
        return global_;
    }

    public void setGlobal_(boolean global_) {
        this.global_ = global_;
    }


}