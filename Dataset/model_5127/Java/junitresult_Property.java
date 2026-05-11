





import java.util.List;
import java.util.ArrayList;

public class junitresult_Property  {

    private String name;
    private String value;





    private junitresult_Testsuite junitresult_testsuite;


    public junitresult_Property(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public junitresult_Testsuite getJunitresult_testsuite() {
        return junitresult_testsuite;
    }

    public void setJunitresult_testsuite(junitresult_Testsuite junitresult_testsuite) {
        this.junitresult_testsuite = junitresult_testsuite;
    }

}