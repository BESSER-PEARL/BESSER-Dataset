





import java.util.List;
import java.util.ArrayList;

public class r2_CO extends QTY {

    private String value;





    private r2_CD r2_cd;


    public r2_CO(
        String value    ) {
        super(
        );
        this.value = value;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public r2_CD getR2_cd() {
        return r2_cd;
    }

    public void setR2_cd(r2_CD r2_cd) {
        this.r2_cd = r2_cd;
    }

}