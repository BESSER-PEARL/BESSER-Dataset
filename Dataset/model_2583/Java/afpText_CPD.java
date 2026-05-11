





import java.util.List;
import java.util.ArrayList;

public class afpText_CPD extends structuredField {

    private String GCGIDLen;
    private String NumCdPts;
    private String CPDesc;
    private String CPGID;
    private String EncScheme;
    private String GCSGID;



    public afpText_CPD(
        String GCGIDLen,        String NumCdPts,        String CPDesc,        String CPGID,        String EncScheme,        String GCSGID    ) {
        super(
        );
        this.GCGIDLen = GCGIDLen;
        this.NumCdPts = NumCdPts;
        this.CPDesc = CPDesc;
        this.CPGID = CPGID;
        this.EncScheme = EncScheme;
        this.GCSGID = GCSGID;
    }


    public String getGcgidlen() {
        return GCGIDLen;
    }

    public void setGcgidlen(String GCGIDLen) {
        this.GCGIDLen = GCGIDLen;
    }
    public String getNumcdpts() {
        return NumCdPts;
    }

    public void setNumcdpts(String NumCdPts) {
        this.NumCdPts = NumCdPts;
    }
    public String getCpdesc() {
        return CPDesc;
    }

    public void setCpdesc(String CPDesc) {
        this.CPDesc = CPDesc;
    }
    public String getCpgid() {
        return CPGID;
    }

    public void setCpgid(String CPGID) {
        this.CPGID = CPGID;
    }
    public String getEncscheme() {
        return EncScheme;
    }

    public void setEncscheme(String EncScheme) {
        this.EncScheme = EncScheme;
    }
    public String getGcsgid() {
        return GCSGID;
    }

    public void setGcsgid(String GCSGID) {
        this.GCSGID = GCSGID;
    }


}