





import java.util.List;
import java.util.ArrayList;

public class ptn104_AbstractNode  {

    private String name;





    private ptn104_Place ptn104_place;


    public ptn104_AbstractNode(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public ptn104_Place getPtn104_place() {
        return ptn104_place;
    }

    public void setPtn104_place(ptn104_Place ptn104_place) {
        this.ptn104_place = ptn104_place;
    }

}