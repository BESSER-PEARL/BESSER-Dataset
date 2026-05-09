





import java.util.List;
import java.util.ArrayList;

public class petriNetEMF_Identification  {

    private String ID;
    private String name;



    public petriNetEMF_Identification(
        String ID,        String name    ) {
        this.ID = ID;
        this.name = name;
    }


    public String getId() {
        return ID;
    }

    public void setId(String ID) {
        this.ID = ID;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }


}