





import java.util.List;
import java.util.ArrayList;

public class testbidirectionalrelation_ConceptE  {






    private testbidirectionalrelation_ConceptA testbidirectionalrelation_concepta;




    private testbidirectionalrelation_ConceptD testbidirectionalrelation_conceptd;




    private List<testbidirectionalrelation_ConceptD> testbidirectionalrelation_conceptds;


    public testbidirectionalrelation_ConceptE(
    ) {
        this.testbidirectionalrelation_conceptds = new ArrayList<>();
    }

    public testbidirectionalrelation_ConceptE(
        ArrayList<testbidirectionalrelation_ConceptD> testbidirectionalrelation_conceptds    ) {
        this.testbidirectionalrelation_conceptds = testbidirectionalrelation_conceptds;
    }


    public testbidirectionalrelation_ConceptA getTestbidirectionalrelation_concepta() {
        return testbidirectionalrelation_concepta;
    }

    public void setTestbidirectionalrelation_concepta(testbidirectionalrelation_ConceptA testbidirectionalrelation_concepta) {
        this.testbidirectionalrelation_concepta = testbidirectionalrelation_concepta;
    }
    public testbidirectionalrelation_ConceptD getTestbidirectionalrelation_conceptd() {
        return testbidirectionalrelation_conceptd;
    }

    public void setTestbidirectionalrelation_conceptd(testbidirectionalrelation_ConceptD testbidirectionalrelation_conceptd) {
        this.testbidirectionalrelation_conceptd = testbidirectionalrelation_conceptd;
    }
    public List<testbidirectionalrelation_ConceptD> getTestbidirectionalrelation_conceptds() {
        return testbidirectionalrelation_conceptds;
    }

    public void addTestbidirectionalrelation_conceptd(Testbidirectionalrelation_conceptd testbidirectionalrelation_conceptd) {
        this.testbidirectionalrelation_conceptds.add(testbidirectionalrelation_conceptd);
    }

}