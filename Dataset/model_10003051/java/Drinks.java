





import java.util.List;
import java.util.ArrayList;

public class Drinks  {

    private String cocktail;
    private String beer;
    private String wine;
    private String spirits;
    private String softDrink;





    private Order order;


    public Drinks(
        String cocktail,        String beer,        String wine,        String spirits,        String softDrink    ) {
        this.cocktail = cocktail;
        this.beer = beer;
        this.wine = wine;
        this.spirits = spirits;
        this.softDrink = softDrink;
    }


    public String getCocktail() {
        return cocktail;
    }

    public void setCocktail(String cocktail) {
        this.cocktail = cocktail;
    }
    public String getBeer() {
        return beer;
    }

    public void setBeer(String beer) {
        this.beer = beer;
    }
    public String getWine() {
        return wine;
    }

    public void setWine(String wine) {
        this.wine = wine;
    }
    public String getSpirits() {
        return spirits;
    }

    public void setSpirits(String spirits) {
        this.spirits = spirits;
    }
    public String getSoftdrink() {
        return softDrink;
    }

    public void setSoftdrink(String softDrink) {
        this.softDrink = softDrink;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}