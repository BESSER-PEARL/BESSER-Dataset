




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class extlibrary_Periodical extends extlibrary_Item {

    private String title;
    private int issuesPerYear;



    public extlibrary_Periodical(
        String title,        int issuesPerYear    ) {
        super(
            LocalDate,            publicationDate        );
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