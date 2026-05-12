





import java.util.List;
import java.util.ArrayList;

public class itm_IssueCategory  {

    private String name;





    private itm_Project itm_project;


    public itm_IssueCategory(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public itm_Project getItm_project() {
        return itm_project;
    }

    public void setItm_project(itm_Project itm_project) {
        this.itm_project = itm_project;
    }

}