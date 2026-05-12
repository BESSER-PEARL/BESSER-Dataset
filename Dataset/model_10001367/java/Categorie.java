





import java.util.List;
import java.util.ArrayList;

public class Categorie  {






    private List<Product> products;


    public Categorie(
    ) {
        this.products = new ArrayList<>();
    }

    public Categorie(
        ArrayList<Product> products    ) {
        this.products = products;
    }


    public List<Product> getProducts() {
        return products;
    }

    public void addProduct(Product product) {
        this.products.add(product);
    }

}