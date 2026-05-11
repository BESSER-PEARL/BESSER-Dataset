





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_EmptyArrayDecl extends Statement {

    private boolean global_;
    private int size;
    private String varName;



    public dinkiemodel_EmptyArrayDecl(
        boolean global_,        int size,        String varName    ) {
        super(
        );
        this.global_ = global_;
        this.size = size;
        this.varName = varName;
    }


    public boolean getGlobal_() {
        return global_;
    }

    public void setGlobal_(boolean global_) {
        this.global_ = global_;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }
    public String getVarname() {
        return varName;
    }

    public void setVarname(String varName) {
        this.varName = varName;
    }


}