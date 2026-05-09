





import java.util.List;
import java.util.ArrayList;

public class NHSM_State  {

    private String name;
    private int memRequirement;



    public NHSM_State(
        String name,        int memRequirement    ) {
        this.name = name;
        this.memRequirement = memRequirement;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getMemrequirement() {
        return memRequirement;
    }

    public void setMemrequirement(int memRequirement) {
        this.memRequirement = memRequirement;
    }


}