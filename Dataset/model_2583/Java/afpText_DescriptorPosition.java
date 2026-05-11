





import java.util.List;
import java.util.ArrayList;

public class afpText_DescriptorPosition extends triplet {

    private String DesPosID;



    public afpText_DescriptorPosition(
        String DesPosID    ) {
        super(
        );
        this.DesPosID = DesPosID;
    }


    public String getDesposid() {
        return DesPosID;
    }

    public void setDesposid(String DesPosID) {
        this.DesPosID = DesPosID;
    }


}