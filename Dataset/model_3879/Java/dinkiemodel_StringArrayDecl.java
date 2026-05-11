





import java.util.List;
import java.util.ArrayList;

public class dinkiemodel_StringArrayDecl extends Statement {

    private String varName;
    private boolean global_;
    private String content;



    public dinkiemodel_StringArrayDecl(
        String varName,        boolean global_,        String content    ) {
        super(
        );
        this.varName = varName;
        this.global_ = global_;
        this.content = content;
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
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}