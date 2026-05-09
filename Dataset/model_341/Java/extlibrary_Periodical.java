





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Periodical extends Item {

    private int issuesPerYear;
    private String title;



    public extlibrary_Periodical(
        int issuesPerYear,        String title    ) {
        super(
        );
        this.issuesPerYear = issuesPerYear;
        this.title = title;
    }


    public int getIssuesperyear() {
        return issuesPerYear;
    }

    public void setIssuesperyear(int issuesPerYear) {
        this.issuesPerYear = issuesPerYear;
    }
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}