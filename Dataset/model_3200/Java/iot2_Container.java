





import java.util.List;
import java.util.ArrayList;

public class iot2_Container extends Contained {






    private iot2_Contained iot2_contained;




    private List<iot2_Contained> iot2_containeds;


    public iot2_Container(
    ) {
        super(
        );
        this.iot2_containeds = new ArrayList<>();
    }

    public iot2_Container(
        ArrayList<iot2_Contained> iot2_containeds    ) {
        this.iot2_containeds = iot2_containeds;
    }


    public iot2_Contained getIot2_contained() {
        return iot2_contained;
    }

    public void setIot2_contained(iot2_Contained iot2_contained) {
        this.iot2_contained = iot2_contained;
    }
    public List<iot2_Contained> getIot2_containeds() {
        return iot2_containeds;
    }

    public void addIot2_contained(Iot2_contained iot2_contained) {
        this.iot2_containeds.add(iot2_contained);
    }

}