





import java.util.List;
import java.util.ArrayList;

public class petrinet_Token  {

    private String name;





    private petrinet_Place petrinet_place;


    public petrinet_Token(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinet_Place getPetrinet_place() {
        return petrinet_place;
    }

    public void setPetrinet_place(petrinet_Place petrinet_place) {
        this.petrinet_place = petrinet_place;
    }

}