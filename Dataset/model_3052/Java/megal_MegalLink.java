





import java.util.List;
import java.util.ArrayList;

public class megal_MegalLink extends MegalElement {

    private String to;





    private megal_MegalFile megal_megalfile;


    public megal_MegalLink(
        String to    ) {
        super(
        );
        this.to = to;
    }


    public String getTo() {
        return to;
    }

    public void setTo(String to) {
        this.to = to;
    }

    public megal_MegalFile getMegal_megalfile() {
        return megal_megalfile;
    }

    public void setMegal_megalfile(megal_MegalFile megal_megalfile) {
        this.megal_megalfile = megal_megalfile;
    }

}