





import java.util.List;
import java.util.ArrayList;

public class afpText_MODCAInterchangeSet extends triplet {

    private String IStype;
    private String ISid;



    public afpText_MODCAInterchangeSet(
        String IStype,        String ISid    ) {
        super(
        );
        this.IStype = IStype;
        this.ISid = ISid;
    }


    public String getIstype() {
        return IStype;
    }

    public void setIstype(String IStype) {
        this.IStype = IStype;
    }
    public String getIsid() {
        return ISid;
    }

    public void setIsid(String ISid) {
        this.ISid = ISid;
    }


}