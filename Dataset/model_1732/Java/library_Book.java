





import java.util.List;
import java.util.ArrayList;

public class library_Book extends Item {

    private int numPages;



    public library_Book(
        int numPages    ) {
        super(
        );
        this.numPages = numPages;
    }


    public int getNumpages() {
        return numPages;
    }

    public void setNumpages(int numPages) {
        this.numPages = numPages;
    }


}