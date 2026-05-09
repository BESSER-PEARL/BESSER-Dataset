





import java.util.List;
import java.util.ArrayList;

public class morel_Unit  {






    private List<morel_EDataType> morel_edatatypes;


    public morel_Unit(
    ) {
        this.morel_edatatypes = new ArrayList<>();
    }

    public morel_Unit(
        ArrayList<morel_EDataType> morel_edatatypes    ) {
        this.morel_edatatypes = morel_edatatypes;
    }


    public List<morel_EDataType> getMorel_edatatypes() {
        return morel_edatatypes;
    }

    public void addMorel_edatatype(Morel_edatatype morel_edatatype) {
        this.morel_edatatypes.add(morel_edatatype);
    }

}