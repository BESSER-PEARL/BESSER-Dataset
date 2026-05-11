





import java.util.List;
import java.util.ArrayList;

public class p2_Configuration extends ModelElement {

    private String wS;
    private String oS;
    private String arch;



    public p2_Configuration(
        String wS,        String oS,        String arch    ) {
        super(
        );
        this.wS = wS;
        this.oS = oS;
        this.arch = arch;
    }


    public String getWs() {
        return wS;
    }

    public void setWs(String wS) {
        this.wS = wS;
    }
    public String getOs() {
        return oS;
    }

    public void setOs(String oS) {
        this.oS = oS;
    }
    public String getArch() {
        return arch;
    }

    public void setArch(String arch) {
        this.arch = arch;
    }


}