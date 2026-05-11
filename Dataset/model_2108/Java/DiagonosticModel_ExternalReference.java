





import java.util.List;
import java.util.ArrayList;

public class DiagonosticModel_ExternalReference  {

    private String owner;
    private String title;
    private String type;
    private String url;





    private DiagonosticModel_TestCase diagonosticmodel_testcase;




    private DiagonosticModel_TestGroup diagonosticmodel_testgroup;


    public DiagonosticModel_ExternalReference(
        String owner,        String title,        String type,        String url    ) {
        this.owner = owner;
        this.title = title;
        this.type = type;
        this.url = url;
    }


    public String getOwner() {
        return owner;
    }

    public void setOwner(String owner) {
        this.owner = owner;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
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
    public DiagonosticModel_TestGroup getDiagonosticmodel_testgroup() {
        return diagonosticmodel_testgroup;
    }

    public void setDiagonosticmodel_testgroup(DiagonosticModel_TestGroup diagonosticmodel_testgroup) {
        this.diagonosticmodel_testgroup = diagonosticmodel_testgroup;
    }

}