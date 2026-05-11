





import java.util.List;
import java.util.ArrayList;

public class testbidirectionalrelation_ConceptA  {






    private List<testbidirectionalrelation_ConceptG> testbidirectionalrelation_conceptgs;




    private List<testbidirectionalrelation_ConceptF> testbidirectionalrelation_conceptfs;


    public testbidirectionalrelation_ConceptA(
    ) {
        this.testbidirectionalrelation_conceptgs = new ArrayList<>();
        this.testbidirectionalrelation_conceptfs = new ArrayList<>();
    }

    public testbidirectionalrelation_ConceptA(
        ArrayList<testbidirectionalrelation_ConceptG> testbidirectionalrelation_conceptgs,        ArrayList<testbidirectionalrelation_ConceptF> testbidirectionalrelation_conceptfs    ) {
        this.testbidirectionalrelation_conceptgs = testbidirectionalrelation_conceptgs;
        this.testbidirectionalrelation_conceptfs = testbidirectionalrelation_conceptfs;
    }


    public List<testbidirectionalrelation_ConceptG> getTestbidirectionalrelation_conceptgs() {
        return testbidirectionalrelation_conceptgs;
    }

    public void addTestbidirectionalrelation_conceptg(Testbidirectionalrelation_conceptg testbidirectionalrelation_conceptg) {
        this.testbidirectionalrelation_conceptgs.add(testbidirectionalrelation_conceptg);
    }
    public List<testbidirectionalrelation_ConceptF> getTestbidirectionalrelation_conceptfs() {
        return testbidirectionalrelation_conceptfs;
    }

    public void addTestbidirectionalrelation_conceptf(Testbidirectionalrelation_conceptf testbidirectionalrelation_conceptf) {
        this.testbidirectionalrelation_conceptfs.add(testbidirectionalrelation_conceptf);
    }

}