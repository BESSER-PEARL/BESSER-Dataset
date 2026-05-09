





import java.util.List;
import java.util.ArrayList;

public class extlibrary_Book extends _9M9ys29IEeGekPcBm25hwQ, _15LbQG60EeGkd4g88tZXfA {

    private int pages;
    private String category;
    private String subtitle;



    public extlibrary_Book(
        int pages,        String category,        String subtitle    ) {
        super(
        );
        this.pages = pages;
        this.category = category;
        this.subtitle = subtitle;
    }


    public int getPages() {
        return pages;
    }

    public void setPages(int pages) {
        this.pages = pages;
    }
    public String getCategory() {
        return category;
    }

    public void setCategory(String category) {
        this.category = category;
    }
    public String getSubtitle() {
        return subtitle;
    }

    public void setSubtitle(String subtitle) {
        this.subtitle = subtitle;
    }


}