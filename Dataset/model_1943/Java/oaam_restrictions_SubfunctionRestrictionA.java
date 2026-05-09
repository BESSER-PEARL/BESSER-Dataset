





import java.util.List;
import java.util.ArrayList;

public class oaam_restrictions_SubfunctionRestrictionA  {






    private List<Subfunctions> subfunctionss;


    public oaam_restrictions_SubfunctionRestrictionA(
    ) {
        this.subfunctionss = new ArrayList<>();
    }

    public oaam_restrictions_SubfunctionRestrictionA(
        ArrayList<Subfunctions> subfunctionss    ) {
        this.subfunctionss = subfunctionss;
    }


    public List<Subfunctions> getSubfunctionss() {
        return subfunctionss;
    }

    public void addSubfunctions(Subfunctions subfunctions) {
        this.subfunctionss.add(subfunctions);
    }

}