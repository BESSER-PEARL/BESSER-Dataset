





import java.util.List;
import java.util.ArrayList;

public class afpText_ECA extends structuredField {

    private String CATName;



    public afpText_ECA(
        String CATName    ) {
        super(
        );
        this.CATName = CATName;
    }


    public String getCatname() {
        return CATName;
    }

    public void setCatname(String CATName) {
        this.CATName = CATName;
    }


}