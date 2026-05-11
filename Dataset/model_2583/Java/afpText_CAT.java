





import java.util.List;
import java.util.ArrayList;

public class afpText_CAT extends structuredField {

    private String CATData;



    public afpText_CAT(
        String CATData    ) {
        super(
        );
        this.CATData = CATData;
    }


    public String getCatdata() {
        return CATData;
    }

    public void setCatdata(String CATData) {
        this.CATData = CATData;
    }


}