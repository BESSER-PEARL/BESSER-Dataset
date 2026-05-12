




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class ShoppingCart  {

    private None Items_list_;
    private LocalDate _attr;



    public ShoppingCart(
        None Items_list_,        LocalDate _attr    ) {
        this.Items_list_ = Items_list_;
        this._attr = _attr;
    }


    public None getItems_list_() {
        return Items_list_;
    }

    public void setItems_list_(None Items_list_) {
        this.Items_list_ = Items_list_;
    }
    public LocalDate get_attr() {
        return _attr;
    }

    public void set_attr(LocalDate _attr) {
        this._attr = _attr;
    }


}