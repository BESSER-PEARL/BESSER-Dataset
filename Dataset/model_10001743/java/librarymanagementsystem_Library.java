





import java.util.List;
import java.util.ArrayList;

public class librarymanagementsystem_Library  {

    private String CDs;
    private String fine;
    private String software;
    private String videos;
    private int computers;
    private String books;
    private String maxFine;



    public librarymanagementsystem_Library(
        String CDs,        String fine,        String software,        String videos,        int computers,        String books,        String maxFine    ) {
        this.CDs = CDs;
        this.fine = fine;
        this.software = software;
        this.videos = videos;
        this.computers = computers;
        this.books = books;
        this.maxFine = maxFine;
    }


    public String getCds() {
        return CDs;
    }

    public void setCds(String CDs) {
        this.CDs = CDs;
    }
    public String getFine() {
        return fine;
    }

    public void setFine(String fine) {
        this.fine = fine;
    }
    public String getSoftware() {
        return software;
    }

    public void setSoftware(String software) {
        this.software = software;
    }
    public String getVideos() {
        return videos;
    }

    public void setVideos(String videos) {
        this.videos = videos;
    }
    public int getComputers() {
        return computers;
    }

    public void setComputers(int computers) {
        this.computers = computers;
    }
    public String getBooks() {
        return books;
    }

    public void setBooks(String books) {
        this.books = books;
    }
    public String getMaxfine() {
        return maxFine;
    }

    public void setMaxfine(String maxFine) {
        this.maxFine = maxFine;
    }


}