





import java.util.List;
import java.util.ArrayList;

public class afpText_ObjectCount extends triplet {

    private String SObjNum;
    private String SobjNmHi;
    private String SubObj;



    public afpText_ObjectCount(
        String SObjNum,        String SobjNmHi,        String SubObj    ) {
        super(
        );
        this.SObjNum = SObjNum;
        this.SobjNmHi = SobjNmHi;
        this.SubObj = SubObj;
    }


    public String getSobjnum() {
        return SObjNum;
    }

    public void setSobjnum(String SObjNum) {
        this.SObjNum = SObjNum;
    }
    public String getSobjnmhi() {
        return SobjNmHi;
    }

    public void setSobjnmhi(String SobjNmHi) {
        this.SobjNmHi = SobjNmHi;
    }
    public String getSubobj() {
        return SubObj;
    }

    public void setSubobj(String SubObj) {
        this.SubObj = SubObj;
    }


}