





import java.util.List;
import java.util.ArrayList;

public class sedml_sedML  {

    private int version;
    private int level;



    public sedml_sedML(
        int version,        int level    ) {
        this.version = version;
        this.level = level;
    }


    public int getVersion() {
        return version;
    }

    public void setVersion(int version) {
        this.version = version;
    }
    public int getLevel() {
        return level;
    }

    public void setLevel(int level) {
        this.level = level;
    }


}