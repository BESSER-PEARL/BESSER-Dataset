





import java.util.List;
import java.util.ArrayList;

public class ConceptASE_Switch extends Trackelement {

    private String Switch_actualState;



    public ConceptASE_Switch(
        String Switch_actualState    ) {
        super(
        );
        this.Switch_actualState = Switch_actualState;
    }


    public String getSwitch_actualstate() {
        return Switch_actualState;
    }

    public void setSwitch_actualstate(String Switch_actualState) {
        this.Switch_actualState = Switch_actualState;
    }


}