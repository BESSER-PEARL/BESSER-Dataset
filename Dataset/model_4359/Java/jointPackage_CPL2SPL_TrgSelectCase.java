





import java.util.List;
import java.util.ArrayList;

public class jointPackage_CPL2SPL_TrgSelectCase extends TrgSelectMember {






    private List<TrgConstant> trgconstants;


    public jointPackage_CPL2SPL_TrgSelectCase(
    ) {
        super(
        );
        this.trgconstants = new ArrayList<>();
    }

    public jointPackage_CPL2SPL_TrgSelectCase(
        ArrayList<TrgConstant> trgconstants    ) {
        this.trgconstants = trgconstants;
    }


    public List<TrgConstant> getTrgconstants() {
        return trgconstants;
    }

    public void addTrgconstant(Trgconstant trgconstant) {
        this.trgconstants.add(trgconstant);
    }

}