





import java.util.List;
import java.util.ArrayList;

public class testcompat103_EClass0 extends NamedElement {






    private testcompat103_World testcompat103_world;




    private List<testcompat103_EClass1> testcompat103_eclass1s;


    public testcompat103_EClass0(
    ) {
        super(
        );
        this.testcompat103_eclass1s = new ArrayList<>();
    }

    public testcompat103_EClass0(
        ArrayList<testcompat103_EClass1> testcompat103_eclass1s    ) {
        this.testcompat103_eclass1s = testcompat103_eclass1s;
    }


    public testcompat103_World getTestcompat103_world() {
        return testcompat103_world;
    }

    public void setTestcompat103_world(testcompat103_World testcompat103_world) {
        this.testcompat103_world = testcompat103_world;
    }
    public List<testcompat103_EClass1> getTestcompat103_eclass1s() {
        return testcompat103_eclass1s;
    }

    public void addTestcompat103_eclass1(Testcompat103_eclass1 testcompat103_eclass1) {
        this.testcompat103_eclass1s.add(testcompat103_eclass1);
    }

}