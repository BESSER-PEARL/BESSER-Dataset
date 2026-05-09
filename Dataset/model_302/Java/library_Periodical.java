





import java.util.List;
import java.util.ArrayList;

public class library_Periodical extends Item {

    private String title;
    private int issuesPerYear;



    public library_Periodical(
        String title,        int issuesPerYear    ) {
        super(
        );
        this.title = title;
        this.issuesPerYear = issuesPerYear;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getIssuesperyear() {
        return issuesPerYear;
    }

    public void setIssuesperyear(int issuesPerYear) {
        this.issuesPerYear = issuesPerYear;
    }


}