





import java.util.List;
import java.util.ArrayList;

public class mission_Drone extends NamedElement {

    private String type;
    private boolean returnHome;



    public mission_Drone(
        String type,        boolean returnHome    ) {
        super(
        );
        this.type = type;
        this.returnHome = returnHome;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public boolean getReturnhome() {
        return returnHome;
    }

    public void setReturnhome(boolean returnHome) {
        this.returnHome = returnHome;
    }


}