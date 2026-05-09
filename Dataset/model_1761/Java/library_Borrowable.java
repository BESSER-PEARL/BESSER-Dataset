





import java.util.List;
import java.util.ArrayList;

public class library_Borrowable  {

    private String title;
    private int copiesAvailable;



    public library_Borrowable(
        String title,        int copiesAvailable    ) {
        this.title = title;
        this.copiesAvailable = copiesAvailable;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public int getCopiesavailable() {
        return copiesAvailable;
    }

    public void setCopiesavailable(int copiesAvailable) {
        this.copiesAvailable = copiesAvailable;
    }


}