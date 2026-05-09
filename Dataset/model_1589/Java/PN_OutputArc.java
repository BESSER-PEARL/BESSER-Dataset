





import java.util.List;
import java.util.ArrayList;

public class PN_OutputArc extends Arc {






    private PN_Place pn_place;


    public PN_OutputArc(
    ) {
        super(
        );
    }



    public PN_Place getPn_place() {
        return pn_place;
    }

    public void setPn_place(PN_Place pn_place) {
        this.pn_place = pn_place;
    }

}