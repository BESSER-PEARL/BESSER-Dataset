





import java.util.List;
import java.util.ArrayList;

public class bookOrder_BookOrder  {

    private String info;





    private bookOrder_Universe bookorder_universe;


    public bookOrder_BookOrder(
        String info    ) {
        this.info = info;
    }


    public String getInfo() {
        return info;
    }

    public void setInfo(String info) {
        this.info = info;
    }

    public bookOrder_Universe getBookorder_universe() {
        return bookorder_universe;
    }

    public void setBookorder_universe(bookOrder_Universe bookorder_universe) {
        this.bookorder_universe = bookorder_universe;
    }

}