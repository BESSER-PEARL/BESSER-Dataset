





import java.util.List;
import java.util.ArrayList;

public class uml_Pin extends ObjectNode, MultiplicityElement {

    private String isControl;



    public uml_Pin(
        String isControl    ) {
        super(
        );
        this.isControl = isControl;
    }


    public String getIscontrol() {
        return isControl;
    }

    public void setIscontrol(String isControl) {
        this.isControl = isControl;
    }


}