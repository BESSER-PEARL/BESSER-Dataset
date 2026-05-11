





import java.util.List;
import java.util.ArrayList;

public class Maude_LabelMapping extends RenMapping {

    private String to;
    private String from_;



    public Maude_LabelMapping(
        String to,        String from_    ) {
        super(
        );
        this.to = to;
        this.from_ = from_;
    }


    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }
    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }


}