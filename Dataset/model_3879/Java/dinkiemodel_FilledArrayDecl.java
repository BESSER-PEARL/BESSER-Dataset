





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_FilledArrayDecl extends Statement {

    private boolean global_;
    private String varName;



    public dinkiemodel_FilledArrayDecl(
        boolean global_,        String varName    ) {
        super(
        );
        this.global_ = global_;
        this.varName = varName;
    }


    public boolean getGlobal_() {
        return global_;
    }

    public void setGlobal_(boolean global_) {
        this.global_ = global_;
    }
    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }


}