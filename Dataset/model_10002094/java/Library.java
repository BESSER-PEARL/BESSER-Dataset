





import java.util.List;
import java.util.ArrayList;

public class Library  {

    private String software;
    private None finePerDar;
    private None maxFine;
    private String computers;
    private String videos;
    private String book;
    private String CDs;
    private String Magazine;



    public Library(
        String software,        None finePerDar,        None maxFine,        String computers,        String videos,        String book,        String CDs,        String Magazine    ) {
        this.software = software;
        this.finePerDar = finePerDar;
        this.maxFine = maxFine;
        this.computers = computers;
        this.videos = videos;
        this.book = book;
        this.CDs = CDs;
        this.Magazine = Magazine;
    }


    public String getSoftware() {
        return software;
    }

    public void setSoftware(String software) {
        this.software = software;
    }
    public None getFineperdar() {
        return finePerDar;
    }

    public void setFineperdar(None finePerDar) {
        this.finePerDar = finePerDar;
    }
    public None getMaxfine() {
        return maxFine;
    }

    public void setMaxfine(None maxFine) {
        this.maxFine = maxFine;
    }
    public String getComputers() {
        return computers;
    }

    public void setComputers(String computers) {
        this.computers = computers;
    }
    public String getVideos() {
        return videos;
    }

    public void setVideos(String videos) {
        this.videos = videos;
    }
    public String getBook() {
        return book;
    }

    public void setBook(String book) {
        this.book = book;
    }
    public String getCds() {
        return CDs;
    }

    public void setCds(String CDs) {
        this.CDs = CDs;
    }
    public String getMagazine() {
        return Magazine;
    }

    public void setMagazine(String Magazine) {
        this.Magazine = Magazine;
    }


}