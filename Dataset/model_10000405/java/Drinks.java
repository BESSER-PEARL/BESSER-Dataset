





import java.util.List;
import java.util.ArrayList;

public class Drinks  {

    private String cocktail;
    private String beer;
    private String spirits;
    private String softDrink;
    private String wine;





    private Order order;


    public Drinks(
        String cocktail,        String beer,        String spirits,        String softDrink,        String wine    ) {
        this.cocktail = cocktail;
        this.beer = beer;
        this.spirits = spirits;
        this.softDrink = softDrink;
        this.wine = wine;
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
    public String getWine() {
        return wine;
    }

    public void setWine(String wine) {
        this.wine = wine;
    }

    public Order getOrder() {
        return order;
    }

    public void setOrder(Order order) {
        this.order = order;
    }

}