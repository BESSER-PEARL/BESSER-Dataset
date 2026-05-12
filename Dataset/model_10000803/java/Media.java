





import java.util.List;
import java.util.ArrayList;

public class Media  {

    private int refNum;
    private int type;





    private Patron patron;


    public Media(
        int refNum,        int type    ) {
        this.refNum = refNum;
        this.type = type;
    }


    public int getRefnum() {
        return refNum;
    }

    public void setRefnum(int refNum) {
        this.refNum = refNum;
    }
    public int getType() {
        return type;
    }

    public void setType(int type) {
        this.type = type;
    }

    public Patron getPatron() {
        return patron;
    }

    public void setPatron(Patron patron) {
        this.patron = patron;
    }

}