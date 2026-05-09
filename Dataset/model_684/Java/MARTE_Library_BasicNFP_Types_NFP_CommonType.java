





import java.util.List;
import java.util.ArrayList;

public class MARTE_Library_BasicNFP_Types_NFP_CommonType  {

    private String expr;
    private String source;
    private String statQ;
    private String mode;
    private String dir;



    public MARTE_Library_BasicNFP_Types_NFP_CommonType(
        String expr,        String source,        String statQ,        String mode,        String dir    ) {
        this.expr = expr;
        this.source = source;
        this.statQ = statQ;
        this.mode = mode;
        this.dir = dir;
    }


    public String getExpr() {
        return expr;
    }

    public void setExpr(String expr) {
        this.expr = expr;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
    }
    public String getStatq() {
        return statQ;
    }

    public void setStatq(String statQ) {
        this.statQ = statQ;
    }
    public String getMode() {
        return mode;
    }

    public void setMode(String mode) {
        this.mode = mode;
    }
    public String getDir() {
        return dir;
    }

    public void setDir(String dir) {
        this.dir = dir;
    }


}