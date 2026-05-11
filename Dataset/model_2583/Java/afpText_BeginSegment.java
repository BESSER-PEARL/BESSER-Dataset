





import java.util.List;
import java.util.ArrayList;

public class afpText_BeginSegment extends triplet {

    private String SEGNAME;



    public afpText_BeginSegment(
        String SEGNAME    ) {
        super(
        );
        this.SEGNAME = SEGNAME;
    }


    public String getSegname() {
        return SEGNAME;
    }

    public void setSegname(String SEGNAME) {
        this.SEGNAME = SEGNAME;
    }


}