





import java.util.List;
import java.util.ArrayList;

public class p2_Configuration extends ModelElement {

    private String arch;
    private String oS;
    private String wS;



    public p2_Configuration(
        String arch,        String oS,        String wS    ) {
        super(
        );
        this.arch = arch;
        this.oS = oS;
        this.wS = wS;
    }


    public String getArch() {
        return arch;
    }

    public void setArch(String arch) {
        this.arch = arch;
    }
    public String getOs() {
        return oS;
    }

    public void setOs(String oS) {
        this.oS = oS;
    }
    public String getWs() {
        return wS;
    }

    public void setWs(String wS) {
        this.wS = wS;
    }


}