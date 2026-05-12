





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_UpdateStatement extends DMLStatement {

    private String conflictResolution;



    public sqliteModel_UpdateStatement(
        String conflictResolution    ) {
        super(
        );
        this.conflictResolution = conflictResolution;
    }


    public String getConflictresolution() {
        return conflictResolution;
    }

    public void setConflictresolution(String conflictResolution) {
        this.conflictResolution = conflictResolution;
    }


}