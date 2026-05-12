





import java.util.List;
import java.util.ArrayList;

public class stext_EventDefinition extends Event {

    private String direction;
    private String type;





    private stext_EventDerivation stext_eventderivation;


    public stext_EventDefinition(
        String direction,        String type    ) {
        super(
        );
        this.direction = direction;
        this.type = type;
    }


    public String getDirection() {
        return direction;
    }

    public void setDirection(String direction) {
        this.direction = direction;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public stext_EventDerivation getStext_eventderivation() {
        return stext_eventderivation;
    }

    public void setStext_eventderivation(stext_EventDerivation stext_eventderivation) {
        this.stext_eventderivation = stext_eventderivation;
    }

}