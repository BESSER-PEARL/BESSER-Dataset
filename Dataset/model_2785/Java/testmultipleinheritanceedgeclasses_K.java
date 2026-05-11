





import java.util.List;
import java.util.ArrayList;

public class testmultipleinheritanceedgeclasses_K  {






    private List<testmultipleinheritanceedgeclasses_EdgeKL> testmultipleinheritanceedgeclasses_edgekls;


    public testmultipleinheritanceedgeclasses_K(
    ) {
        this.testmultipleinheritanceedgeclasses_edgekls = new ArrayList<>();
    }

    public testmultipleinheritanceedgeclasses_K(
        ArrayList<testmultipleinheritanceedgeclasses_EdgeKL> testmultipleinheritanceedgeclasses_edgekls    ) {
        this.testmultipleinheritanceedgeclasses_edgekls = testmultipleinheritanceedgeclasses_edgekls;
    }


    public List<testmultipleinheritanceedgeclasses_EdgeKL> getTestmultipleinheritanceedgeclasses_edgekls() {
        return testmultipleinheritanceedgeclasses_edgekls;
    }

    public void addTestmultipleinheritanceedgeclasses_edgekl(Testmultipleinheritanceedgeclasses_edgekl testmultipleinheritanceedgeclasses_edgekl) {
        this.testmultipleinheritanceedgeclasses_edgekls.add(testmultipleinheritanceedgeclasses_edgekl);
    }

}