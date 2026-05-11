





import java.util.List;
import java.util.ArrayList;

public class adb_AcceptStatement extends CompoundStatement {

    private String entryidentifier;





    private adb_FormalPart adb_formalpart;




    private adb_HandledSequenceOfStatements adb_handledsequenceofstatements;




    private adb_EntryDeclaration adb_entrydeclaration;


    public adb_AcceptStatement(
        String entryidentifier    ) {
        super(
        );
        this.entryidentifier = entryidentifier;
    }


    public String getEntryidentifier() {
        return entryidentifier;
    }

    public void setEntryidentifier(String entryidentifier) {
        this.entryidentifier = entryidentifier;
    }

    public adb_FormalPart getAdb_formalpart() {
        return adb_formalpart;
    }

    public void setAdb_formalpart(adb_FormalPart adb_formalpart) {
        this.adb_formalpart = adb_formalpart;
    }
    public adb_HandledSequenceOfStatements getAdb_handledsequenceofstatements() {
        return adb_handledsequenceofstatements;
    }

    public void setAdb_handledsequenceofstatements(adb_HandledSequenceOfStatements adb_handledsequenceofstatements) {
        this.adb_handledsequenceofstatements = adb_handledsequenceofstatements;
    }
    public adb_EntryDeclaration getAdb_entrydeclaration() {
        return adb_entrydeclaration;
    }

    public void setAdb_entrydeclaration(adb_EntryDeclaration adb_entrydeclaration) {
        this.adb_entrydeclaration = adb_entrydeclaration;
    }

}