





import java.util.List;
import java.util.ArrayList;

public class cobol_handlers_AtEndOfPage extends Handler {

    private String eop;



    public cobol_handlers_AtEndOfPage(
        String eop    ) {
        super(
        );
        this.eop = eop;
    }


    public String getEop() {
        return eop;
    }

    public void setEop(String eop) {
        this.eop = eop;
    }


}