





import java.util.List;
import java.util.ArrayList;

public class testbidirectionalrelation_ConceptG  {






    private List<testbidirectionalrelation_ConceptF> testbidirectionalrelation_conceptfs;




    private testbidirectionalrelation_ConceptF testbidirectionalrelation_conceptf;


    public testbidirectionalrelation_ConceptG(
    ) {
        this.testbidirectionalrelation_conceptfs = new ArrayList<>();
    }

    public testbidirectionalrelation_ConceptG(
        ArrayList<testbidirectionalrelation_ConceptF> testbidirectionalrelation_conceptfs    ) {
        this.testbidirectionalrelation_conceptfs = testbidirectionalrelation_conceptfs;
    }


    public List<testbidirectionalrelation_ConceptF> getTestbidirectionalrelation_conceptfs() {
        return testbidirectionalrelation_conceptfs;
    }

    public void addTestbidirectionalrelation_conceptf(Testbidirectionalrelation_conceptf testbidirectionalrelation_conceptf) {
        this.testbidirectionalrelation_conceptfs.add(testbidirectionalrelation_conceptf);
    }
    public testbidirectionalrelation_ConceptF getTestbidirectionalrelation_conceptf() {
        return testbidirectionalrelation_conceptf;
    }

    public void setTestbidirectionalrelation_conceptf(testbidirectionalrelation_ConceptF testbidirectionalrelation_conceptf) {
        this.testbidirectionalrelation_conceptf = testbidirectionalrelation_conceptf;
    }

}