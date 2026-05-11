





import java.util.List;
import java.util.ArrayList;

public class fiacre_RecordElem extends Exp {

    private String field;





    private fiacre_Exp fiacre_exp;


    public fiacre_RecordElem(
        String field    ) {
        super(
        );
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

}