





import java.util.List;
import java.util.ArrayList;

public class afpText_LLE extends structuredField {

    private String LnkType;



    public afpText_LLE(
        String LnkType    ) {
        super(
        );
        this.LnkType = LnkType;
    }


    public String getLnktype() {
        return LnkType;
    }

    public void setLnktype(String LnkType) {
        this.LnkType = LnkType;
    }


}