





import java.util.List;
import java.util.ArrayList;

public class afpText_ObjectStructuredFieldExtent extends triplet {

    private String SFExt;
    private String SFExtHi;



    public afpText_ObjectStructuredFieldExtent(
        String SFExt,        String SFExtHi    ) {
        super(
        );
        this.SFExt = SFExt;
        this.SFExtHi = SFExtHi;
    }


    public String getSfext() {
        return SFExt;
    }

    public void setSfext(String SFExt) {
        this.SFExt = SFExt;
    }
    public String getSfexthi() {
        return SFExtHi;
    }

    public void setSfexthi(String SFExtHi) {
        this.SFExtHi = SFExtHi;
    }


}