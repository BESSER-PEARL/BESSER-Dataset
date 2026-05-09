





import java.util.List;
import java.util.ArrayList;

public class petrinet2_Element  {

    private String name;





    private petrinet2_Petrinet petrinet2_petrinet;


    public petrinet2_Element(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public petrinet2_Petrinet getPetrinet2_petrinet() {
        return petrinet2_petrinet;
    }

    public void setPetrinet2_petrinet(petrinet2_Petrinet petrinet2_petrinet) {
        this.petrinet2_petrinet = petrinet2_petrinet;
    }

}