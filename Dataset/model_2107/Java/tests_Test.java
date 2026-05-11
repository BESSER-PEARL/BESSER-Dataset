





import java.util.List;
import java.util.ArrayList;

public class tests_Test  {

    private String version;
    private String id;





    private tests_TestsModel tests_testsmodel;


    public tests_Test(
        String version,        String id    ) {
        this.version = version;
        this.id = id;
    }


    public String getVersion() {
        return version;
    }

    public void setVersion(String version) {
        this.version = version;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public tests_TestsModel getTests_testsmodel() {
        return tests_testsmodel;
    }

    public void setTests_testsmodel(tests_TestsModel tests_testsmodel) {
        this.tests_testsmodel = tests_testsmodel;
    }

}