





import java.util.List;
import java.util.ArrayList;

public class afpText_EFG extends structuredField {

    private String FEGName;



    public afpText_EFG(
        String FEGName    ) {
        super(
        );
        this.FEGName = FEGName;
    }


    public String getFegname() {
        return FEGName;
    }

    public void setFegname(String FEGName) {
        this.FEGName = FEGName;
    }


}