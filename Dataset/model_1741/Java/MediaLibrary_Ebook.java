





import java.util.List;
import java.util.ArrayList;

public class MediaLibrary_Ebook extends Artifact {

    private int pages;



    public MediaLibrary_Ebook(
        int pages    ) {
        super(
        );
        this.pages = pages;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }


}