





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String description;
    private String name;





    private Visitor visitor;




    private Account account;




    private ShoppingCart shoppingcart;




    private List<LineItem> lineitems;


    public Product(
        String description,        String name    ) {
        this.description = description;
        this.name = name;
        this.lineitems = new ArrayList<>();
    }

    public Product(
        String description,        String name        ArrayList<LineItem> lineitems    ) {
        this.description = description;
        this.name = name;
        this.lineitems = lineitems;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Visitor getVisitor() {
        return visitor;
    }

    public void setVisitor(Visitor visitor) {
        this.visitor = visitor;
    }
    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }
    public List<LineItem> getLineitems() {
        return lineitems;
    }

    public void addLineitem(Lineitem lineitem) {
        this.lineitems.add(lineitem);
    }

}