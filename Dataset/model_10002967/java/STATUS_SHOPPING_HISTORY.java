





import java.util.List;
import java.util.ArrayList;

public class STATUS_SHOPPING_HISTORY  {

    private String _id;
    private String name;





    private SHOPPING_HISTORY shopping_history;


    public STATUS_SHOPPING_HISTORY(
        String _id,        String name    ) {
        this._id = _id;
        this.name = name;
    }


    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public SHOPPING_HISTORY getShopping_history() {
        return shopping_history;
    }

    public void setShopping_history(SHOPPING_HISTORY shopping_history) {
        this.shopping_history = shopping_history;
    }

}