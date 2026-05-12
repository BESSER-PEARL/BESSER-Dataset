





import java.util.List;
import java.util.ArrayList;

public class Drinks  {

    private String softDrink;
    private String spirits;
    private String beer;
    private String wine;
    private String cocktail;





    private Order order;


    public Drinks(
        String softDrink,        String spirits,        String beer,        String wine,        String cocktail    ) {
        this.softDrink = softDrink;
        this.spirits = spirits;
        this.beer = beer;
        this.wine = wine;
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
    public String getCocktail() {
        return cocktail;
    }

    public void setCocktail(String cocktail) {
        this.cocktail = cocktail;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}