





import java.util.List;
import java.util.ArrayList;

public class Product  {

    private String name;
    private String description;





    private Account account;




    private List<LineItem> lineitems;




    private Visitor visitor;




    private ShoppingCart shoppingcart;


    public Product(
        String name,        String description    ) {
        this.name = name;
        this.description = description;
        this.lineitems = new ArrayList<>();
    }

    public Product(
        String name,        String description        ArrayList<LineItem> lineitems    ) {
        this.name = name;
        this.description = description;
        this.lineitems = lineitems;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public Account getAccount() {
        return account;
    }

    public void setAccount(Account account) {
        this.account = account;
    }
    public List<LineItem> getLineitems() {
        return lineitems;
    }

    public void addLineitem(Lineitem lineitem) {
        this.lineitems.add(lineitem);
    }
    public Visitor getVisitor() {
        return visitor;
    }

    public void setVisitor(Visitor visitor) {
        this.visitor = visitor;
    }
    public ShoppingCart getShoppingcart() {
        return shoppingcart;
    }

    public void setShoppingcart(ShoppingCart shoppingcart) {
        this.shoppingcart = shoppingcart;
    }

}