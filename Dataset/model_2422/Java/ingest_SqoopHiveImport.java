





import java.util.List;
import java.util.ArrayList;

public class ingest_SqoopHiveImport extends SqoopImport {

    private String targetHiveTable;
    private String targetHiveDatabase;



    public ingest_SqoopHiveImport(
        String targetHiveTable,        String targetHiveDatabase    ) {
        super(
        );
        this.targetHiveTable = targetHiveTable;
        this.targetHiveDatabase = targetHiveDatabase;
    }


    public String getTargethivetable() {
        return targetHiveTable;
    }

    public void setTargethivetable(String targetHiveTable) {
        this.targetHiveTable = targetHiveTable;
    }
    public String getTargethivedatabase() {
        return targetHiveDatabase;
    }

    public void setTargethivedatabase(String targetHiveDatabase) {
        this.targetHiveDatabase = targetHiveDatabase;
    }


}