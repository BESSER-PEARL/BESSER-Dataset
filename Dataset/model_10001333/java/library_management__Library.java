





import java.util.List;
import java.util.ArrayList;

public class library_management__Library  {

    private String Videos;
    private String Computers;
    private String CD;
    private String Books;
    private String Softwares;



    public library_management__Library(
        String Videos,        String Computers,        String CD,        String Books,        String Softwares    ) {
        this.Videos = Videos;
        this.Computers = Computers;
        this.CD = CD;
        this.Books = Books;
        this.Softwares = Softwares;
    }


    public String getVideos() {
        return Videos;
    }

    public void setVideos(String Videos) {
        this.Videos = Videos;
    }
    public String getComputers() {
        return Computers;
    }

    public void setComputers(String Computers) {
        this.Computers = Computers;
    }
    public String getCd() {
        return CD;
    }

    public void setCd(String CD) {
        this.CD = CD;
    }
    public String getBooks() {
        return Books;
    }

    public void setBooks(String Books) {
        this.Books = Books;
    }
    public String getSoftwares() {
        return Softwares;
    }

    public void setSoftwares(String Softwares) {
        this.Softwares = Softwares;
    }


}