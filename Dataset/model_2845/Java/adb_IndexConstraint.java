





import java.util.List;
import java.util.ArrayList;

public class adb_IndexConstraint extends CompositeConstraint {






    private List<adb_DiscreteRange> adb_discreteranges;


    public adb_IndexConstraint(
    ) {
        super(
        );
        this.adb_discreteranges = new ArrayList<>();
    }

    public adb_IndexConstraint(
        ArrayList<adb_DiscreteRange> adb_discreteranges    ) {
        this.adb_discreteranges = adb_discreteranges;
    }


    public List<adb_DiscreteRange> getAdb_discreteranges() {
        return adb_discreteranges;
    }

    public void addAdb_discreterange(Adb_discreterange adb_discreterange) {
        this.adb_discreteranges.add(adb_discreterange);
    }

}