





import java.util.List;
import java.util.ArrayList;

public class coom_Version  {

    private int majorMalue;
    private int minorValue;





    private coom_ComponentOnOffManifest coom_componentonoffmanifest;


    public coom_Version(
        int majorMalue,        int minorValue    ) {
        this.majorMalue = majorMalue;
        this.minorValue = minorValue;
    }


    public int getMajormalue() {
        return majorMalue;
    }

    public void setMajormalue(int majorMalue) {
        this.majorMalue = majorMalue;
    }
    public int getMinorvalue() {
        return minorValue;
    }

    public void setMinorvalue(int minorValue) {
        this.minorValue = minorValue;
    }

    public coom_ComponentOnOffManifest getCoom_componentonoffmanifest() {
        return coom_componentonoffmanifest;
    }

    public void setCoom_componentonoffmanifest(coom_ComponentOnOffManifest coom_componentonoffmanifest) {
        this.coom_componentonoffmanifest = coom_componentonoffmanifest;
    }

}