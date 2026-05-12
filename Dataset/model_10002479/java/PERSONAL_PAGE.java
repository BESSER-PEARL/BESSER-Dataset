





import java.util.List;
import java.util.ArrayList;

public class PERSONAL_PAGE  {

    private int YEAR;
    private String BRANCH;



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


}