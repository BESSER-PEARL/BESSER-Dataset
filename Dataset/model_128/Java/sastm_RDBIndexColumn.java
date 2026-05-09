





import java.util.List;
import java.util.ArrayList;

public class sastm_RDBIndexColumn extends OtherSyntaxObject {

    private String AscendingOrDescending;



    public sastm_RDBIndexColumn(
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