





import java.util.List;
import java.util.ArrayList;

public class ACADEMIC_PAGE  {

    private String BRANCH;
    private String STUDIES;





    private List<PERSONAL_PAGE> personal_pages;


    public ACADEMIC_PAGE(
        String BRANCH,        String STUDIES    ) {
        this.BRANCH = BRANCH;
        this.STUDIES = STUDIES;
        this.personal_pages = new ArrayList<>();
    }

    public ACADEMIC_PAGE(
        String BRANCH,        String STUDIES        ArrayList<PERSONAL_PAGE> personal_pages    ) {
        this.BRANCH = BRANCH;
        this.STUDIES = STUDIES;
        this.personal_pages = personal_pages;
    }

    public String getBranch() {
        return BRANCH;
    }

    public void setBranch(String BRANCH) {
        this.BRANCH = BRANCH;
    }
    public String getStudies() {
        return STUDIES;
    }

    public void setStudies(String STUDIES) {
        this.STUDIES = STUDIES;
    }

    public List<PERSONAL_PAGE> getPersonal_pages() {
        return personal_pages;
    }

    public void addPersonal_page(Personal_page personal_page) {
        this.personal_pages.add(personal_page);
    }

}