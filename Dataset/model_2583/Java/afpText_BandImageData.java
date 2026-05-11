





import java.util.List;
import java.util.ArrayList;

public class afpText_BandImageData extends triplet {

    private String DATA;
    private String RESERVED;
    private String BANDNUM;



    public afpText_BandImageData(
        String DATA,        String RESERVED,        String BANDNUM    ) {
        super(
        );
        this.DATA = DATA;
        this.RESERVED = RESERVED;
        this.BANDNUM = BANDNUM;
    }


    public String getData() {
        return DATA;
    }

    public void setData(String DATA) {
        this.DATA = DATA;
    }
    public String getReserved() {
        return RESERVED;
    }

    public void setReserved(String RESERVED) {
        this.RESERVED = RESERVED;
    }
    public String getBandnum() {
        return BANDNUM;
    }

    public void setBandnum(String BANDNUM) {
        this.BANDNUM = BANDNUM;
    }


}