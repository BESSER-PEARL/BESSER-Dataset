





import java.util.List;
import java.util.ArrayList;

public class afpText_EGR extends structuredField {

    private String GdoName;



    public afpText_EGR(
        String GdoName    ) {
        super(
        );
        this.GdoName = GdoName;
    }


    public String getGdoname() {
        return GdoName;
    }

    public void setGdoname(String GdoName) {
        this.GdoName = GdoName;
    }


}