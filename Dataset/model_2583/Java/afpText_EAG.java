





import java.util.List;
import java.util.ArrayList;

public class afpText_EAG extends structuredField {

    private String AEGName;



    public afpText_EAG(
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