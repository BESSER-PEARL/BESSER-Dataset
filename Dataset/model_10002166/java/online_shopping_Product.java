





import java.util.List;
import java.util.ArrayList;

public class online_shopping_Product  {

    private String Product_ID;
    private None Description;
    private None Name;
    private None Image_File_Name;
    private String Price;





    private online_shopping_Category online_shopping_category;




    private List<online_shopping_Shopping_Card> online_shopping_shopping_cards;


    public online_shopping_Product(
        String Product_ID,        None Description,        None Name,        None Image_File_Name,        String Price    ) {
        this.Product_ID = Product_ID;
        this.Description = Description;
        this.Name = Name;
        this.Image_File_Name = Image_File_Name;
        this.Price = Price;
        this.online_shopping_shopping_cards = new ArrayList<>();
    }

    public online_shopping_Product(
        String Product_ID,        None Description,        None Name,        None Image_File_Name,        String Price        ArrayList<online_shopping_Shopping_Card> online_shopping_shopping_cards    ) {
        this.Product_ID = Product_ID;
        this.Description = Description;
        this.Name = Name;
        this.Image_File_Name = Image_File_Name;
        this.Price = Price;
        this.online_shopping_shopping_cards = online_shopping_shopping_cards;
    }

    public String getProduct_id() {
        return Product_ID;
    }

    public void setProduct_id(String Product_ID) {
        this.Product_ID = Product_ID;
    }
    public None getDescription() {
        return Description;
    }

    public void setDescription(None Description) {
        this.Description = Description;
    }
    public None getName() {
        return Name;
    }

    public void setName(None Name) {
        this.Name = Name;
    }
    public None getImage_file_name() {
        return Image_File_Name;
    }

    public void setImage_file_name(None Image_File_Name) {
        this.Image_File_Name = Image_File_Name;
    }
    public String getPrice() {
        return Price;
    }

    public void setPrice(String Price) {
        this.Price = Price;
    }

    public online_shopping_Category getOnline_shopping_category() {
        return online_shopping_category;
    }

    public void setOnline_shopping_category(online_shopping_Category online_shopping_category) {
        this.online_shopping_category = online_shopping_category;
    }
    public List<online_shopping_Shopping_Card> getOnline_shopping_shopping_cards() {
        return online_shopping_shopping_cards;
    }

    public void addOnline_shopping_shopping_card(Online_shopping_shopping_card online_shopping_shopping_card) {
        this.online_shopping_shopping_cards.add(online_shopping_shopping_card);
    }

}