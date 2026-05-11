





import java.util.List;
import java.util.ArrayList;

public class aadl2_ContainmentPathElement extends Element {

    private String annexName;





    private List<aadl2_ArrayRange> aadl2_arrayranges;


    public aadl2_ContainmentPathElement(
        String annexName    ) {
        super(
        );
        this.annexName = annexName;
        this.aadl2_arrayranges = new ArrayList<>();
    }

    public aadl2_ContainmentPathElement(
        String annexName        ArrayList<aadl2_ArrayRange> aadl2_arrayranges    ) {
        this.annexName = annexName;
        this.aadl2_arrayranges = aadl2_arrayranges;
    }

    public String getAnnexname() {
        return annexName;
    }

    public void setAnnexname(String annexName) {
        this.annexName = annexName;
    }

    public List<aadl2_ArrayRange> getAadl2_arrayranges() {
        return aadl2_arrayranges;
    }

    public void addAadl2_arrayrange(Aadl2_arrayrange aadl2_arrayrange) {
        this.aadl2_arrayranges.add(aadl2_arrayrange);
    }

}