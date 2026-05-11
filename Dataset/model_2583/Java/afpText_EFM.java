





import java.util.List;
import java.util.ArrayList;

public class afpText_EFM extends structuredField {

    private String FMName;



    public afpText_EFM(
        String FMName    ) {
        super(
        );
        this.FMName = FMName;
    }


    public String getFmname() {
        return FMName;
    }

    public void setFmname(String FMName) {
        this.FMName = FMName;
    }


}