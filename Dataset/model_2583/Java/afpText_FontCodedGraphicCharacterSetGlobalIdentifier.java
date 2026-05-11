





import java.util.List;
import java.util.ArrayList;

public class afpText_FontCodedGraphicCharacterSetGlobalIdentifier extends triplet {

    private String CPGID;
    private String GCSGID;



    public afpText_FontCodedGraphicCharacterSetGlobalIdentifier(
        String CPGID,        String GCSGID    ) {
        super(
        );
        this.CPGID = CPGID;
        this.GCSGID = GCSGID;
    }


    public String getCpgid() {
        return CPGID;
    }

    public void setCpgid(String CPGID) {
        this.CPGID = CPGID;
    }
    public String getGcsgid() {
        return GCSGID;
    }

    public void setGcsgid(String GCSGID) {
        this.GCSGID = GCSGID;
    }


}