





import java.util.List;
import java.util.ArrayList;

public class internalsm_TimeConstraint  {

    private String type;





    private internalsm_State internalsm_state;


    public internalsm_TimeConstraint(
        String type    ) {
        this.type = type;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public internalsm_State getInternalsm_state() {
        return internalsm_state;
    }

    public void setInternalsm_state(internalsm_State internalsm_state) {
        this.internalsm_state = internalsm_state;
    }

}