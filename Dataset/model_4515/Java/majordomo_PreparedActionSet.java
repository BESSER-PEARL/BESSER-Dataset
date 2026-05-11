





import java.util.List;
import java.util.ArrayList;

public class majordomo_PreparedActionSet  {

    private String name;





    private majordomo_ActionSetReference majordomo_actionsetreference;


    public majordomo_PreparedActionSet(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public majordomo_ActionSetReference getMajordomo_actionsetreference() {
        return majordomo_actionsetreference;
    }

    public void setMajordomo_actionsetreference(majordomo_ActionSetReference majordomo_actionsetreference) {
        this.majordomo_actionsetreference = majordomo_actionsetreference;
    }

}