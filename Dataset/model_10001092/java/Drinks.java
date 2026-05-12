





import java.util.List;
import java.util.ArrayList;

public class Drinks  {

    private String wine;
    private String beer;
    private String cocktail;
    private String softDrink;
    private String spirits;





    private Order order;


    public Drinks(
        String wine,        String beer,        String cocktail,        String softDrink,        String spirits    ) {
        this.wine = wine;
        this.beer = beer;
        this.cocktail = cocktail;
        this.softDrink = softDrink;
        this.spirits = spirits;
    }


    public String getWine() {
        return wine;
    }

    public void setWine(String wine) {
        this.wine = wine;
    }
    public String getBeer() {
        return beer;
    }

    public void setBeer(String beer) {
        this.beer = beer;
    }
    public String getCocktail() {
        return cocktail;
    }

    public void setCocktail(String cocktail) {
        this.cocktail = cocktail;
    }
    public String getSoftdrink() {
        return softDrink;
    }

    public void setSoftdrink(String softDrink) {
        this.softDrink = softDrink;
    }
    public String getSpirits() {
        return spirits;
    }

    public void setSpirits(String spirits) {
        this.spirits = spirits;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}