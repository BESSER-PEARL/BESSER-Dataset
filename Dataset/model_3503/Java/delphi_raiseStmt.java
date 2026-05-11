





import java.util.List;
import java.util.ArrayList;

public class delphi_raiseStmt extends structStmt {

    private String at;
    private String raise_;



    public delphi_raiseStmt(
        String at,        String raise_    ) {
        super(
        );
        this.at = at;
        this.raise_ = raise_;
    }


    public String getAt() {
        return at;
    }

    public void setAt(String at) {
        this.at = at;
    }
    public String getRaise_() {
        return raise_;
    }

    public void setRaise_(String raise_) {
        this.raise_ = raise_;
    }


}