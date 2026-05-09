





import java.util.List;
import java.util.ArrayList;

public class extlibraryprofile_Periodical extends Item {

    private String issuesPerYear;



    public extlibraryprofile_Periodical(
        String issuesPerYear    ) {
        super(
        );
        this.issuesPerYear = issuesPerYear;
    }


    public String getIssuesperyear() {
        return issuesPerYear;
    }

    public void setIssuesperyear(String issuesPerYear) {
        this.issuesPerYear = issuesPerYear;
    }


}