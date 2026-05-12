





import java.util.List;
import java.util.ArrayList;

public class kbuild_Target extends BuildEntry {






    private List<kbuild_Values> kbuild_valuess;




    private kbuild_Values kbuild_values;


    public kbuild_Target(
    ) {
        super(
        );
        this.kbuild_valuess = new ArrayList<>();
    }

    public kbuild_Target(
        ArrayList<kbuild_Values> kbuild_valuess    ) {
        this.kbuild_valuess = kbuild_valuess;
    }


    public List<kbuild_Values> getKbuild_valuess() {
        return kbuild_valuess;
    }

    public void addKbuild_values(Kbuild_values kbuild_values) {
        this.kbuild_valuess.add(kbuild_values);
    }
    public kbuild_Values getKbuild_values() {
        return kbuild_values;
    }

    public void setKbuild_values(kbuild_Values kbuild_values) {
        this.kbuild_values = kbuild_values;
    }

}