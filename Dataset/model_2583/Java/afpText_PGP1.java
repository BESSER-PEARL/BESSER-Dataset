





import java.util.List;
import java.util.ArrayList;

public class afpText_PGP1 extends structuredField {

    private String XOset;
    private String YOset;



    public afpText_PGP1(
        String XOset,        String YOset    ) {
        super(
        );
        this.XOset = XOset;
        this.YOset = YOset;
    }


    public String getXoset() {
        return XOset;
    }

    public void setXoset(String XOset) {
        this.XOset = XOset;
    }
    public String getYoset() {
        return YOset;
    }

    public void setYoset(String YOset) {
        this.YOset = YOset;
    }


}