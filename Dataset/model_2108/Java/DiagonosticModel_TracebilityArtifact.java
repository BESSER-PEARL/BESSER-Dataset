





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_TracebilityArtifact  {

    private String type;
    private String url;





    private DiagonosticModel_TestCase diagonosticmodel_testcase;


    public DiagonosticModel_TracebilityArtifact(
        String type,        String url    ) {
        this.type = type;
        this.url = url;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getUrl() {
        return url;
    }

    public void setUrl(String url) {
        this.url = url;
    }

    public DiagonosticModel_TestCase getDiagonosticmodel_testcase() {
        return diagonosticmodel_testcase;
    }

    public void setDiagonosticmodel_testcase(DiagonosticModel_TestCase diagonosticmodel_testcase) {
        this.diagonosticmodel_testcase = diagonosticmodel_testcase;
    }

}