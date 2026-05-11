





import java.util.List;
import java.util.ArrayList;

public class dmx_DmxBaseTypeSet  {

    private String members;
    private String name;



    public dmx_DmxBaseTypeSet(
        String members,        String name    ) {
        this.members = members;
        this.name = name;
    }


    public String getMembers() {
        return members;
    }

    public void setMembers(String members) {
        this.members = members;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}