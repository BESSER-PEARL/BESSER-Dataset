





import java.util.List;
import java.util.ArrayList;

public class Dish  {

    private String _attr;





    private Menu1 menu1;




    private List<Menu1> menu1s;


    public Dish(
        String _attr    ) {
        this._attr = _attr;
        this.menu1s = new ArrayList<>();
    }

    public Dish(
        String _attr        ArrayList<Menu1> menu1s    ) {
        this._attr = _attr;
        this.menu1s = menu1s;
    }

    public String get_attr() {
        return _attr;
    }

    public void set_attr(String _attr) {
        this._attr = _attr;
    }

    public Menu1 getMenu1() {
        return menu1;
    }

    public void setMenu1(Menu1 menu1) {
        this.menu1 = menu1;
    }
    public List<Menu1> getMenu1s() {
        return menu1s;
    }

    public void addMenu1(Menu1 menu1) {
        this.menu1s.add(menu1);
    }

}