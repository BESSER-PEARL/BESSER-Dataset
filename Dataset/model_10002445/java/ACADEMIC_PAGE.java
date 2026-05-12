





import java.util.List;
import java.util.ArrayList;

public class ACADEMIC_PAGE  {

    private String STUDIES;
    private String BRANCH;





    private WELCOME_PAGE welcome_page;


    public ACADEMIC_PAGE(
        String STUDIES,        String BRANCH    ) {
        this.STUDIES = STUDIES;
        this.BRANCH = BRANCH;
    }


    public String getStudies() {
        return STUDIES;
    }

    public void setStudies(String STUDIES) {
        this.STUDIES = STUDIES;
    }
    public String getBranch() {
        return BRANCH;
    }

    public void setBranch(String BRANCH) {
        this.BRANCH = BRANCH;
    }

    public WELCOME_PAGE getWelcome_page() {
        return welcome_page;
    }

    public void setWelcome_page(WELCOME_PAGE welcome_page) {
        this.welcome_page = welcome_page;
    }

}