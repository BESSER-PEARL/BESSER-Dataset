





import java.util.List;
import java.util.ArrayList;

public class afpText_ENG extends structuredField {

    private String PGrpName;



    public afpText_ENG(
        String PGrpName    ) {
        super(
        );
        this.PGrpName = PGrpName;
    }


    public String getPgrpname() {
        return PGrpName;
    }

    public void setPgrpname(String PGrpName) {
        this.PGrpName = PGrpName;
    }


}