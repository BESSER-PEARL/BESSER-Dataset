





import java.util.List;
import java.util.ArrayList;

public class adb_LoopStatement extends CompoundStatement {

    private String sameName;
    private String name;





    private adb_ExitStatement adb_exitstatement;




    private adb_SequenceOfStatements adb_sequenceofstatements;


    public adb_LoopStatement(
        String sameName,        String name    ) {
        super(
        );
        this.sameName = sameName;
        this.name = name;
    }


    public String getSamename() {
        return sameName;
    }

    public void setSamename(String sameName) {
        this.sameName = sameName;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public adb_ExitStatement getAdb_exitstatement() {
        return adb_exitstatement;
    }

    public void setAdb_exitstatement(adb_ExitStatement adb_exitstatement) {
        this.adb_exitstatement = adb_exitstatement;
    }
    public adb_SequenceOfStatements getAdb_sequenceofstatements() {
        return adb_sequenceofstatements;
    }

    public void setAdb_sequenceofstatements(adb_SequenceOfStatements adb_sequenceofstatements) {
        this.adb_sequenceofstatements = adb_sequenceofstatements;
    }

}