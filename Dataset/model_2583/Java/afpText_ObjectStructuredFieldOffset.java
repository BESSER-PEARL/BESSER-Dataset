





import java.util.List;
import java.util.ArrayList;

public class afpText_ObjectStructuredFieldOffset extends triplet {

    private String SFOff;
    private String SFOffHi;



    public afpText_ObjectStructuredFieldOffset(
        String SFOff,        String SFOffHi    ) {
        super(
        );
        this.SFOff = SFOff;
        this.SFOffHi = SFOffHi;
    }


    public String getSfoff() {
        return SFOff;
    }

    public void setSfoff(String SFOff) {
        this.SFOff = SFOff;
    }
    public String getSfoffhi() {
        return SFOffHi;
    }

    public void setSfoffhi(String SFOffHi) {
        this.SFOffHi = SFOffHi;
    }


}