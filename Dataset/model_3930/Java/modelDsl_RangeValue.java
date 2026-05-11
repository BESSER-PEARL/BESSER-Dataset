





import java.util.List;
import java.util.ArrayList;

public class modelDsl_RangeValue extends Value {

    private boolean toInf;
    private int to;
    private boolean fromInf;
    private int from_;



    public modelDsl_RangeValue(
        boolean toInf,        int to,        boolean fromInf,        int from_    ) {
        super(
        );
        this.toInf = toInf;
        this.to = to;
        this.fromInf = fromInf;
        this.from_ = from_;
    }


    public boolean getToinf() {
        return toInf;
    }

    public void setToinf(boolean toInf) {
        this.toInf = toInf;
    }
    public int getTo() {
        return to;
    }

    public void setTo(int to) {
        this.to = to;
    }
    public boolean getFrominf() {
        return fromInf;
    }

    public void setFrominf(boolean fromInf) {
        this.fromInf = fromInf;
    }
    public int getFrom_() {
        return from_;
    }

    public void setFrom_(int from_) {
        this.from_ = from_;
    }


}