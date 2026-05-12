





import java.util.List;
import java.util.ArrayList;

public class bean_CategoryCounts  {

    private int politicsCount;
    private int sportsCount;
    private int educationCount;
    private int entertainmentCount;
    private int historyCount;



    public bean_CategoryCounts(
        int politicsCount,        int sportsCount,        int educationCount,        int entertainmentCount,        int historyCount    ) {
        this.politicsCount = politicsCount;
        this.sportsCount = sportsCount;
        this.educationCount = educationCount;
        this.entertainmentCount = entertainmentCount;
        this.historyCount = historyCount;
    }


    public int getPoliticscount() {
        return politicsCount;
    }

    public void setPoliticscount(int politicsCount) {
        this.politicsCount = politicsCount;
    }
    public int getSportscount() {
        return sportsCount;
    }

    public void setSportscount(int sportsCount) {
        this.sportsCount = sportsCount;
    }
    public int getEducationcount() {
        return educationCount;
    }

    public void setEducationcount(int educationCount) {
        this.educationCount = educationCount;
    }
    public int getEntertainmentcount() {
        return entertainmentCount;
    }

    public void setEntertainmentcount(int entertainmentCount) {
        this.entertainmentCount = entertainmentCount;
    }
    public int getHistorycount() {
        return historyCount;
    }

    public void setHistorycount(int historyCount) {
        this.historyCount = historyCount;
    }


}