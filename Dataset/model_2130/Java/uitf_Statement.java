





import java.util.List;
import java.util.ArrayList;

public class uitf_Statement  {

    private String description;
    private String kind;





    private uitf_TestCase uitf_testcase;


    public uitf_Statement(
        String description,        String kind    ) {
        this.description = description;
        this.kind = kind;
    }


    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getKind() {
        return kind;
    }

    public void setKind(String kind) {
        this.kind = kind;
    }

    public uitf_TestCase getUitf_testcase() {
        return uitf_testcase;
    }

    public void setUitf_testcase(uitf_TestCase uitf_testcase) {
        this.uitf_testcase = uitf_testcase;
    }

}