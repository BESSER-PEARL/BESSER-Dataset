





import java.util.List;
import java.util.ArrayList;

public class Drinks  {

    private String beer;
    private String softDrink;
    private String spirits;
    private String cocktail;
    private String wine;





    private Order order;


    public Drinks(
        String beer,        String softDrink,        String spirits,        String cocktail,        String wine    ) {
        this.beer = beer;
        this.softDrink = softDrink;
        this.spirits = spirits;
        this.cocktail = cocktail;
        this.wine = wine;
    }


    public String getBeer() {
        return beer;
    }

    public void setBeer(String beer) {
        this.beer = beer;
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
    public String getCocktail() {
        return cocktail;
    }

    public void setCocktail(String cocktail) {
        this.cocktail = cocktail;
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