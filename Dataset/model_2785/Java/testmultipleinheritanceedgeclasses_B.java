





import java.util.List;
import java.util.ArrayList;

public class testmultipleinheritanceedgeclasses_B  {






    private List<testmultipleinheritanceedgeclasses_EdgeAB> testmultipleinheritanceedgeclasses_edgeabs;




    private testmultipleinheritanceedgeclasses_EdgeAB testmultipleinheritanceedgeclasses_edgeab;


    public testmultipleinheritanceedgeclasses_B(
    ) {
        this.testmultipleinheritanceedgeclasses_edgeabs = new ArrayList<>();
    }

    public testmultipleinheritanceedgeclasses_B(
        ArrayList<testmultipleinheritanceedgeclasses_EdgeAB> testmultipleinheritanceedgeclasses_edgeabs    ) {
        this.testmultipleinheritanceedgeclasses_edgeabs = testmultipleinheritanceedgeclasses_edgeabs;
    }


    public List<testmultipleinheritanceedgeclasses_EdgeAB> getTestmultipleinheritanceedgeclasses_edgeabs() {
        return testmultipleinheritanceedgeclasses_edgeabs;
    }

    public void addTestmultipleinheritanceedgeclasses_edgeab(Testmultipleinheritanceedgeclasses_edgeab testmultipleinheritanceedgeclasses_edgeab) {
        this.testmultipleinheritanceedgeclasses_edgeabs.add(testmultipleinheritanceedgeclasses_edgeab);
    }
    public testmultipleinheritanceedgeclasses_EdgeAB getTestmultipleinheritanceedgeclasses_edgeab() {
        return testmultipleinheritanceedgeclasses_edgeab;
    }

    public void setTestmultipleinheritanceedgeclasses_edgeab(testmultipleinheritanceedgeclasses_EdgeAB testmultipleinheritanceedgeclasses_edgeab) {
        this.testmultipleinheritanceedgeclasses_edgeab = testmultipleinheritanceedgeclasses_edgeab;
    }

}