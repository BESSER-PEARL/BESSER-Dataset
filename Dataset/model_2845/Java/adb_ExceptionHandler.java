





import java.util.List;
import java.util.ArrayList;

public class adb_ExceptionHandler  {

    private String name;





    private List<adb_ExceptionChoice> adb_exceptionchoices;




    private adb_SequenceOfStatements adb_sequenceofstatements;




    private adb_SequenceOfStatements adb_sequenceofstatements;


    public adb_ExceptionHandler(
        String name    ) {
        this.name = name;
        this.adb_exceptionchoices = new ArrayList<>();
    }

    public adb_ExceptionHandler(
        String name        ArrayList<adb_ExceptionChoice> adb_exceptionchoices    ) {
        this.name = name;
        this.adb_exceptionchoices = adb_exceptionchoices;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<adb_ExceptionChoice> getAdb_exceptionchoices() {
        return adb_exceptionchoices;
    }

    public void addAdb_exceptionchoice(Adb_exceptionchoice adb_exceptionchoice) {
        this.adb_exceptionchoices.add(adb_exceptionchoice);
    }
    public adb_SequenceOfStatements getAdb_sequenceofstatements() {
        return adb_sequenceofstatements;
    }

    public void setAdb_sequenceofstatements(adb_SequenceOfStatements adb_sequenceofstatements) {
        this.adb_sequenceofstatements = adb_sequenceofstatements;
    }
    public adb_SequenceOfStatements getAdb_sequenceofstatements() {
        return adb_sequenceofstatements;
    }

    public void setAdb_sequenceofstatements(adb_SequenceOfStatements adb_sequenceofstatements) {
        this.adb_sequenceofstatements = adb_sequenceofstatements;
    }

}