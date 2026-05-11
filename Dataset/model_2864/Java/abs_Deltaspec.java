





import java.util.List;
import java.util.ArrayList;

public class abs_Deltaspec  {

    private String name;
    private String deltaspec_param;



    public abs_Deltaspec(
        String name,        String deltaspec_param    ) {
        this.name = name;
        this.deltaspec_param = deltaspec_param;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDeltaspec_param() {
        return deltaspec_param;
    }

    public void setDeltaspec_param(String deltaspec_param) {
        this.deltaspec_param = deltaspec_param;
    }


}