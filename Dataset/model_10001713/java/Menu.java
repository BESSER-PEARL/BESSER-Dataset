





import java.util.List;
import java.util.ArrayList;

public class Menu  {

    private String _attr;





    private Manager manager;




    private Store store;


    public Menu(
        String _attr    ) {
        this._attr = _attr;
    }


    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }

    public Manager getManager() {
        return manager;
    }

    public void setManager(Manager manager) {
        this.manager = manager;
    }
    public Store getStore() {
        return store;
    }

    public void setStore(Store store) {
        this.store = store;
    }

}