





import java.util.List;
import java.util.ArrayList;

public class shr5Management_PersonaValueChange extends Changes {

    private int to;
    private int from_;



    public shr5Management_PersonaValueChange(
        int to,        int from_    ) {
        super(
        );
        this.to = to;
        this.from_ = from_;
    }


    public int getTo() {
        return to;
    }

    public void setTo(int to) {
        this.to = to;
    }
    public int getFrom_() {
        return from_;
    }

    public void setFrom_(int from_) {
        this.from_ = from_;
    }


}