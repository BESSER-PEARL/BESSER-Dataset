





import java.util.List;
import java.util.ArrayList;

public class Order  {






    private List<Drinks> drinkss;




    private List<Menu> menus;




    private Bill bill;


    public Order(
    ) {
        this.drinkss = new ArrayList<>();
        this.menus = new ArrayList<>();
    }

    public Order(
        ArrayList<Drinks> drinkss,        ArrayList<Menu> menus    ) {
        this.drinkss = drinkss;
        this.menus = menus;
    }


    public List<Drinks> getDrinkss() {
        return drinkss;
    }

    public void addDrinks(Drinks drinks) {
        this.drinkss.add(drinks);
    }
    public List<Menu> getMenus() {
        return menus;
    }

    public void addMenu(Menu menu) {
        this.menus.add(menu);
    }
    public Bill getBill() {
        return bill;
    }

    public void setBill(Bill bill) {
        this.bill = bill;
    }

}