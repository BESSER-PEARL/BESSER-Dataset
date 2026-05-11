





import java.util.List;
import java.util.ArrayList;

public class migrationmodeler_Representation  {

    private String name;





    private migrationmodeler_TestCase migrationmodeler_testcase;


    public migrationmodeler_Representation(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public migrationmodeler_TestCase getMigrationmodeler_testcase() {
        return migrationmodeler_testcase;
    }

    public void setMigrationmodeler_testcase(migrationmodeler_TestCase migrationmodeler_testcase) {
        this.migrationmodeler_testcase = migrationmodeler_testcase;
    }

}