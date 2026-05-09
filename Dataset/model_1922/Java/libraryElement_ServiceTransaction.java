





import java.util.List;
import java.util.ArrayList;

public class libraryElement_ServiceTransaction  {

    private String TestResult;





    private libraryElement_InputPrimitive libraryelement_inputprimitive;




    private libraryElement_ServiceSequence libraryelement_servicesequence;




    private List<libraryElement_OutputPrimitive> libraryelement_outputprimitives;


    public libraryElement_ServiceTransaction(
        String TestResult    ) {
        this.TestResult = TestResult;
        this.libraryelement_outputprimitives = new ArrayList<>();
    }

    public libraryElement_ServiceTransaction(
        String TestResult        ArrayList<libraryElement_OutputPrimitive> libraryelement_outputprimitives    ) {
        this.TestResult = TestResult;
        this.libraryelement_outputprimitives = libraryelement_outputprimitives;
    }

    public String getTestresult() {
        return TestResult;
    }

    public void setTestresult(String TestResult) {
        this.TestResult = TestResult;
    }

    public libraryElement_InputPrimitive getLibraryelement_inputprimitive() {
        return libraryelement_inputprimitive;
    }

    public void setLibraryelement_inputprimitive(libraryElement_InputPrimitive libraryelement_inputprimitive) {
        this.libraryelement_inputprimitive = libraryelement_inputprimitive;
    }
    public libraryElement_ServiceSequence getLibraryelement_servicesequence() {
        return libraryelement_servicesequence;
    }

    public void setLibraryelement_servicesequence(libraryElement_ServiceSequence libraryelement_servicesequence) {
        this.libraryelement_servicesequence = libraryelement_servicesequence;
    }
    public List<libraryElement_OutputPrimitive> getLibraryelement_outputprimitives() {
        return libraryelement_outputprimitives;
    }

    public void addLibraryelement_outputprimitive(Libraryelement_outputprimitive libraryelement_outputprimitive) {
        this.libraryelement_outputprimitives.add(libraryelement_outputprimitive);
    }

}