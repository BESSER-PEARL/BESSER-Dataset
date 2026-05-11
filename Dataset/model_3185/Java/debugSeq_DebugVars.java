





import java.util.List;
import java.util.ArrayList;

public class debugSeq_DebugVars  {

    private String pname;
    private String version;
    private String configfile;





    private debugSeq_DebugSeqModel debugseq_debugseqmodel;


    public debugSeq_DebugVars(
        String pname,        String version,        String configfile    ) {
        this.pname = pname;
        this.version = version;
        this.configfile = configfile;
    }


    public String getPname() {
        return pname;
    }

    public void setPname(String pname) {
        this.pname = pname;
    }
    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getConfigfile() {
        return configfile;
    }

    public void setConfigfile(String configfile) {
        this.configfile = configfile;
    }

    public debugSeq_DebugSeqModel getDebugseq_debugseqmodel() {
        return debugseq_debugseqmodel;
    }

    public void setDebugseq_debugseqmodel(debugSeq_DebugSeqModel debugseq_debugseqmodel) {
        this.debugseq_debugseqmodel = debugseq_debugseqmodel;
    }

}