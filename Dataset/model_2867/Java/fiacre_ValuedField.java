





import java.util.List;
import java.util.ArrayList;

public class fiacre_ValuedField  {

    private String field;





    private fiacre_Exp fiacre_exp;




    private fiacre_InlineRecord fiacre_inlinerecord;


    public fiacre_ValuedField(
        String field    ) {
        this.field = field;
    }


    public String getField() {
        return field;
    }

    public void setField(String field) {
        this.field = field;
    }

    public fiacre_Exp getFiacre_exp() {
        return fiacre_exp;
    }

    public void setFiacre_exp(fiacre_Exp fiacre_exp) {
        this.fiacre_exp = fiacre_exp;
    }
    public fiacre_InlineRecord getFiacre_inlinerecord() {
        return fiacre_inlinerecord;
    }

    public void setFiacre_inlinerecord(fiacre_InlineRecord fiacre_inlinerecord) {
        this.fiacre_inlinerecord = fiacre_inlinerecord;
    }

}