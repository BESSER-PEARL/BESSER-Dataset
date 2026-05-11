





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Result_list extends Component {

    private int number_of_items_per_page;
    private int distance_between_items;





    private webshop_builder_3k_model_Item webshop_builder_3k_model_item;


    public webshop_builder_3k_model_Result_list(
        int number_of_items_per_page,        int distance_between_items    ) {
        super(
        );
        this.number_of_items_per_page = number_of_items_per_page;
        this.distance_between_items = distance_between_items;
    }


    public int getNumber_of_items_per_page() {
        return number_of_items_per_page;
    }

    public void setNumber_of_items_per_page(int number_of_items_per_page) {
        this.number_of_items_per_page = number_of_items_per_page;
    }
    public int getDistance_between_items() {
        return distance_between_items;
    }

    public void setDistance_between_items(int distance_between_items) {
        this.distance_between_items = distance_between_items;
    }

    public webshop_builder_3k_model_Item getWebshop_builder_3k_model_item() {
        return webshop_builder_3k_model_item;
    }

    public void setWebshop_builder_3k_model_item(webshop_builder_3k_model_Item webshop_builder_3k_model_item) {
        this.webshop_builder_3k_model_item = webshop_builder_3k_model_item;
    }

}