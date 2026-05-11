





import java.util.List;
import java.util.ArrayList;

public class afpText_BPT extends structuredField {

    private String PTdoName;



    public afpText_BPT(
        String PTdoName    ) {
        super(
        );
        this.PTdoName = PTdoName;
    }


    public String getPtdoname() {
        return PTdoName;
    }

    public void setPtdoname(String PTdoName) {
        this.PTdoName = PTdoName;
    }


}