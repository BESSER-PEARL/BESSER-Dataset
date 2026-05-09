




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class extlibrary_Periodical extends extlibrary_Item, _9M9ys29IEeGekPcBm25hwQ {

    private int issuesPerYear;



    public extlibrary_Periodical(
        int issuesPerYear    ) {
        super(
            LocalDate,            publicationDate        );
        this.issuesPerYear = issuesPerYear;
    }


    public int getIssuesperyear() {
        return issuesPerYear;
    }

    public void setIssuesperyear(int issuesPerYear) {
        this.issuesPerYear = issuesPerYear;
    }


}