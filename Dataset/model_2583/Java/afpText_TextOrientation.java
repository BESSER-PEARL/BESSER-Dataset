





import java.util.List;
import java.util.ArrayList;

public class afpText_TextOrientation extends triplet {

    private String BAxis;
    private String IAxis;



    public afpText_TextOrientation(
        String BAxis,        String IAxis    ) {
        super(
        );
        this.BAxis = BAxis;
        this.IAxis = IAxis;
    }


    public String getBaxis() {
        return BAxis;
    }

    public void setBaxis(String BAxis) {
        this.BAxis = BAxis;
    }
    public String getIaxis() {
        return IAxis;
    }

    public void setIaxis(String IAxis) {
        this.IAxis = IAxis;
    }


}