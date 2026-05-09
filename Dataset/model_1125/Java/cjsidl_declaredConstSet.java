





import java.util.List;
import java.util.ArrayList;

public class cjsidl_declaredConstSet  {

    private String name;
    private String constName;
    private String constSetVersion;



    public cjsidl_declaredConstSet(
        String name,        String constName,        String constSetVersion    ) {
        this.name = name;
        this.constName = constName;
        this.constSetVersion = constSetVersion;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getConstname() {
        return constName;
    }

    public void setConstname(String constName) {
        this.constName = constName;
    }
    public String getConstsetversion() {
        return constSetVersion;
    }

    public void setConstsetversion(String constSetVersion) {
        this.constSetVersion = constSetVersion;
    }


}