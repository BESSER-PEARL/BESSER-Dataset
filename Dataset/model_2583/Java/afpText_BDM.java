





import java.util.List;
import java.util.ArrayList;

public class afpText_BDM extends structuredField {

    private String DMName;
    private String DatFmt;



    public afpText_BDM(
        String DMName,        String DatFmt    ) {
        super(
        );
        this.DMName = DMName;
        this.DatFmt = DatFmt;
    }


    public String getDmname() {
        return DMName;
    }

    public void setDmname(String DMName) {
        this.DMName = DMName;
    }
    public String getDatfmt() {
        return DatFmt;
    }

    public void setDatfmt(String DatFmt) {
        this.DatFmt = DatFmt;
    }


}