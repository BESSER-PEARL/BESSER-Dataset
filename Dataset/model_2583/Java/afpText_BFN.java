





import java.util.List;
import java.util.ArrayList;

public class afpText_BFN extends structuredField {

    private String RSName;



    public afpText_BFN(
        String RSName    ) {
        super(
        );
        this.RSName = RSName;
    }


    public String getRsname() {
        return RSName;
    }

    public void setRsname(String RSName) {
        this.RSName = RSName;
    }


}