





import java.util.List;
import java.util.ArrayList;

public class iec61131_literals_Signed_Integer extends interfaces_Range, st_Case_List_Element, literals_Integer {

    private boolean negative;



    public iec61131_literals_Signed_Integer(
        boolean negative    ) {
        super(
        );
        this.negative = negative;
    }


    public boolean getNegative() {
        return negative;
    }

    public void setNegative(boolean negative) {
        this.negative = negative;
    }


}