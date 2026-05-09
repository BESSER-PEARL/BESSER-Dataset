





import java.util.List;
import java.util.ArrayList;

public class astm_RDBIndexColumn extends OtherSyntaxObject {

    private String AscendingOrDescending;



    public astm_RDBIndexColumn(
        String AscendingOrDescending    ) {
        super(
        );
        this.AscendingOrDescending = AscendingOrDescending;
    }


    public String getAscendingordescending() {
        return AscendingOrDescending;
    }

    public void setAscendingordescending(String AscendingOrDescending) {
        this.AscendingOrDescending = AscendingOrDescending;
    }


}