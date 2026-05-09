





import java.util.List;
import java.util.ArrayList;

public class atem_TaggedText extends ElementType {






    private List<atem_ElementType> atem_elementtypes;


    public atem_TaggedText(
    ) {
        super(
        );
        this.atem_elementtypes = new ArrayList<>();
    }

    public atem_TaggedText(
        ArrayList<atem_ElementType> atem_elementtypes    ) {
        this.atem_elementtypes = atem_elementtypes;
    }


    public List<atem_ElementType> getAtem_elementtypes() {
        return atem_elementtypes;
    }

    public void addAtem_elementtype(Atem_elementtype atem_elementtype) {
        this.atem_elementtypes.add(atem_elementtype);
    }

}