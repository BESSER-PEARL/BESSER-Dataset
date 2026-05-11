





import java.util.List;
import java.util.ArrayList;

public class afpText_IPS extends structuredField {

    private String YpsOset;
    private String XpsOset;
    private String PsegName;



    public afpText_IPS(
        String YpsOset,        String XpsOset,        String PsegName    ) {
        super(
        );
        this.YpsOset = YpsOset;
        this.XpsOset = XpsOset;
        this.PsegName = PsegName;
    }


    public String getYpsoset() {
        return YpsOset;
    }

    public void setYpsoset(String YpsOset) {
        this.YpsOset = YpsOset;
    }
    public String getXpsoset() {
        return XpsOset;
    }

    public void setXpsoset(String XpsOset) {
        this.XpsOset = XpsOset;
    }
    public String getPsegname() {
        return PsegName;
    }

    public void setPsegname(String PsegName) {
        this.PsegName = PsegName;
    }


}