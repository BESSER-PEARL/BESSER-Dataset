





import java.util.List;
import java.util.ArrayList;

public class test_ComplianceAssertion extends Assertion {

    private String path;



    public test_ComplianceAssertion(
        String path    ) {
        super(
        );
        this.path = path;
    }


    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}