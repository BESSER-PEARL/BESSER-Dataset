





import java.util.List;
import java.util.ArrayList;

public class testbidirectionalrelation_ConceptE  {






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