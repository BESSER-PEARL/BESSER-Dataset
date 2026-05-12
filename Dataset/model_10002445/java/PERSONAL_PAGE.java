





import java.util.List;
import java.util.ArrayList;

public class PERSONAL_PAGE  {

    private int YEAR;
    private String BRANCH;





    private WELCOME_PAGE welcome_page;


    public PERSONAL_PAGE(
        int YEAR,        String BRANCH    ) {
        this.YEAR = YEAR;
        this.BRANCH = BRANCH;
    }


    public int getYear() {
        return YEAR;
    }

    public void setYear(int YEAR) {
        this.YEAR = YEAR;
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