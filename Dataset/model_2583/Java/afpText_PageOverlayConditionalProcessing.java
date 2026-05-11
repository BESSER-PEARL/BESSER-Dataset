





import java.util.List;
import java.util.ArrayList;

public class afpText_PageOverlayConditionalProcessing extends triplet {

    private String PgOvType;
    private String Level;



    public afpText_PageOverlayConditionalProcessing(
        String PgOvType,        String Level    ) {
        super(
        );
        this.PgOvType = PgOvType;
        this.Level = Level;
    }


    public String getPgovtype() {
        return PgOvType;
    }

    public void setPgovtype(String PgOvType) {
        this.PgOvType = PgOvType;
    }
    public String getLevel() {
        return Level;
    }

    public void setLevel(String Level) {
        this.Level = Level;
    }


}