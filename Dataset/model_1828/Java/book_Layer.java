





import java.util.List;
import java.util.ArrayList;

public class book_Layer  {

    private boolean visible;





    private book_Page book_page;


    public book_Layer(
        boolean visible    ) {
        this.visible = visible;
    }


    public boolean getVisible() {
        return visible;
    }

    public void setVisible(boolean visible) {
        this.visible = visible;
    }

    public book_Page getBook_page() {
        return book_page;
    }

    public void setBook_page(book_Page book_page) {
        this.book_page = book_page;
    }

}