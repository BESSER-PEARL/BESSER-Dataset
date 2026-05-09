





import java.util.List;
import java.util.ArrayList;

public class mMDSL_BreakContinue  {

    private String break_;
    private String continue_;





    private mMDSL_WhileLoop mmdsl_whileloop;




    private mMDSL_ForLoop mmdsl_forloop;


    public mMDSL_BreakContinue(
        String break_,        String continue_    ) {
        this.break_ = break_;
        this.continue_ = continue_;
    }


    public String getBreak_() {
        return break_;
    }

    public void setBreak_(String break_) {
        this.break_ = break_;
    }
    public String getContinue_() {
        return continue_;
    }

    public void setContinue_(String continue_) {
        this.continue_ = continue_;
    }

    public mMDSL_WhileLoop getMmdsl_whileloop() {
        return mmdsl_whileloop;
    }

    public void setMmdsl_whileloop(mMDSL_WhileLoop mmdsl_whileloop) {
        this.mmdsl_whileloop = mmdsl_whileloop;
    }
    public mMDSL_ForLoop getMmdsl_forloop() {
        return mmdsl_forloop;
    }

    public void setMmdsl_forloop(mMDSL_ForLoop mmdsl_forloop) {
        this.mmdsl_forloop = mmdsl_forloop;
    }

}