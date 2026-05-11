





import java.util.List;
import java.util.ArrayList;

public class adb_ProcedureOrEntryCallStatement extends SimpleStatement, TriggeringStatement {






    private adb_Name adb_name;


    public adb_ProcedureOrEntryCallStatement(
    ) {
        super(
        );
    }



    public adb_Name getAdb_name() {
        return adb_name;
    }

    public void setAdb_name(adb_Name adb_name) {
        this.adb_name = adb_name;
    }

}