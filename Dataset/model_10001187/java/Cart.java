





import java.util.List;
import java.util.ArrayList;

public class Cart  {

    private String Delete_;
    private int Buy_;
    private int No_of_items_;



    public Cart(
        String Delete_,        int Buy_,        int No_of_items_    ) {
        this.Delete_ = Delete_;
        this.Buy_ = Buy_;
        this.No_of_items_ = No_of_items_;
    }


    public String getDelete_() {
        return Delete_;
    }

    public void setDelete_(String Delete_) {
        this.Delete_ = Delete_;
    }
    public int getBuy_() {
        return Buy_;
    }

    public void setBuy_(int Buy_) {
        this.Buy_ = Buy_;
    }
    public int getNo_of_items_() {
        return No_of_items_;
    }

    public void setNo_of_items_(int No_of_items_) {
        this.No_of_items_ = No_of_items_;
    }


}