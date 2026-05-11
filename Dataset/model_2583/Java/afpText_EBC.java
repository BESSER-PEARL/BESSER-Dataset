





import java.util.List;
import java.util.ArrayList;

public class afpText_EBC extends structuredField {

    private String BCdoName;



    public afpText_EBC(
        String BCdoName    ) {
        super(
        );
        this.BCdoName = BCdoName;
    }


    public String getBcdoname() {
        return BCdoName;
    }

    public void setBcdoname(String BCdoName) {
        this.BCdoName = BCdoName;
    }


}