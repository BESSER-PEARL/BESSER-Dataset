





import java.util.List;
import java.util.ArrayList;

public class Maude_LabelMapping extends RenMapping {

    private String from_;
    private String to;



    public Maude_LabelMapping(
        String from_,        String to    ) {
        super(
        );
        this.from_ = from_;
        this.to = to;
    }


    public String getFrom_() {
        return from_;
    }

    public void setFrom_(String from_) {
        this.from_ = from_;
    }
    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }


}