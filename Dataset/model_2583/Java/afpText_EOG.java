





import java.util.List;
import java.util.ArrayList;

public class afpText_EOG extends structuredField {

    private String OEGName;



    public afpText_EOG(
        String OEGName    ) {
        super(
        );
        this.OEGName = OEGName;
    }


    public String getOegname() {
        return OEGName;
    }

    public void setOegname(String OEGName) {
        this.OEGName = OEGName;
    }


}