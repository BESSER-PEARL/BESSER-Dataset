





import java.util.List;
import java.util.ArrayList;

public class uitf_TestSuite  {

    private String id;





    private List<uitf_TestCase> uitf_testcases;


    public uitf_TestSuite(
        String id    ) {
        this.id = id;
        this.uitf_testcases = new ArrayList<>();
    }

    public uitf_TestSuite(
        String id        ArrayList<uitf_TestCase> uitf_testcases    ) {
        this.id = id;
        this.uitf_testcases = uitf_testcases;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public List<uitf_TestCase> getUitf_testcases() {
        return uitf_testcases;
    }

    public void addUitf_testcase(Uitf_testcase uitf_testcase) {
        this.uitf_testcases.add(uitf_testcase);
    }

}