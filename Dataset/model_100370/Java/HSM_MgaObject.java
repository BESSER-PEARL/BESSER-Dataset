





import java.util.List;
import java.util.ArrayList;

public class HSM_MgaObject  {

    private String name;
    private String position;



    public HSM_MgaObject(
        String name,        String position    ) {
        this.name = name;
        this.position = position;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }


}