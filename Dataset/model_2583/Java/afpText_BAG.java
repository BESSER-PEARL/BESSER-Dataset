





import java.util.List;
import java.util.ArrayList;

public class afpText_BAG extends structuredField {

    private String AEGName;



    public afpText_BAG(
        String AEGName    ) {
        super(
        );
        this.AEGName = AEGName;
    }


    public String getAegname() {
        return AEGName;
    }

    public void setAegname(String AEGName) {
        this.AEGName = AEGName;
    }


}