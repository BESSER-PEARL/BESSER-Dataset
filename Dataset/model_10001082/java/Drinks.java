





import java.util.List;
import java.util.ArrayList;

public class Drinks  {

    private String cocktail;
    private String wine;
    private String softDrink;
    private String spirits;
    private String beer;



    public Drinks(
        String cocktail,        String wine,        String softDrink,        String spirits,        String beer    ) {
        this.cocktail = cocktail;
        this.wine = wine;
        this.softDrink = softDrink;
        this.spirits = spirits;
        this.beer = beer;
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


}