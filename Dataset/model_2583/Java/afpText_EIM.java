





import java.util.List;
import java.util.ArrayList;

public class afpText_EIM extends structuredField {

    private String IdoName;



    public afpText_EIM(
        String IdoName    ) {
        super(
        );
        this.IdoName = IdoName;
    }


    public String getIdoname() {
        return IdoName;
    }

    public void setIdoname(String IdoName) {
        this.IdoName = IdoName;
    }


}