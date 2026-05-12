





import java.util.List;
import java.util.ArrayList;

public class FSM_MgaObject  {

    private String position;
    private String name;



    public FSM_MgaObject(
        String position,        String name    ) {
        this.position = position;
        this.name = name;
    }


    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}