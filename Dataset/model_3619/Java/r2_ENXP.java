





import java.util.List;
import java.util.ArrayList;

public class r2_ENXP extends XP {

    private String type;
    private String qualifier;





    private r2_EN r2_en;


    public r2_ENXP(
        String type,        String qualifier    ) {
        super(
        );
        this.type = type;
        this.qualifier = qualifier;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getQualifier() {
        return qualifier;
    }

    public void setQualifier(String qualifier) {
        this.qualifier = qualifier;
    }

    public r2_EN getR2_en() {
        return r2_en;
    }

    public void setR2_en(r2_EN r2_en) {
        this.r2_en = r2_en;
    }

}