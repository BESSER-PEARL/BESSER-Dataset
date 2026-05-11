





import java.util.List;
import java.util.ArrayList;

public class afpText_CGCSGID extends triplet {

    private String GCSGID;
    private String CPGID;



    public afpText_CGCSGID(
        String GCSGID,        String CPGID    ) {
        super(
        );
        this.GCSGID = GCSGID;
        this.CPGID = CPGID;
    }


    public String getGcsgid() {
        return GCSGID;
    }

    public void setGcsgid(String GCSGID) {
        this.GCSGID = GCSGID;
    }
    public String getCpgid() {
        return CPGID;
    }

    public void setCpgid(String CPGID) {
        this.CPGID = CPGID;
    }


}