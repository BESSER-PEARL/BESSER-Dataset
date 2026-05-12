





import java.util.List;
import java.util.ArrayList;

public class Media  {

    private int type;
    private int refNum;





    private Patron patron;


    public Media(
        int type,        int refNum    ) {
        this.type = type;
        this.refNum = refNum;
    }


    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }
    public int getRefnum() {
        return refNum;
    }

    public void setRefnum(int refNum) {
        this.refNum = refNum;
    }

    public Patron getPatron() {
        return patron;
    }

    public void setPatron(Patron patron) {
        this.patron = patron;
    }

}