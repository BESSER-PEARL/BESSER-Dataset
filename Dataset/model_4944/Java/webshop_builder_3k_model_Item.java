





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Item extends Component {






    private webshop_builder_3k_model_Result_list webshop_builder_3k_model_result_list;




    private List<webshop_builder_3k_model_Text_field> webshop_builder_3k_model_text_fields;




    private webshop_builder_3k_model_Picture webshop_builder_3k_model_picture;


    public webshop_builder_3k_model_Item(
    ) {
        super(
        );
        this.webshop_builder_3k_model_text_fields = new ArrayList<>();
    }

    public webshop_builder_3k_model_Item(
        ArrayList<webshop_builder_3k_model_Text_field> webshop_builder_3k_model_text_fields    ) {
        this.webshop_builder_3k_model_text_fields = webshop_builder_3k_model_text_fields;
    }


    public webshop_builder_3k_model_Result_list getWebshop_builder_3k_model_result_list() {
        return webshop_builder_3k_model_result_list;
    }

    public void setWebshop_builder_3k_model_result_list(webshop_builder_3k_model_Result_list webshop_builder_3k_model_result_list) {
        this.webshop_builder_3k_model_result_list = webshop_builder_3k_model_result_list;
    }
    public List<webshop_builder_3k_model_Text_field> getWebshop_builder_3k_model_text_fields() {
        return webshop_builder_3k_model_text_fields;
    }

    public void addWebshop_builder_3k_model_text_field(Webshop_builder_3k_model_text_field webshop_builder_3k_model_text_field) {
        this.webshop_builder_3k_model_text_fields.add(webshop_builder_3k_model_text_field);
    }
    public webshop_builder_3k_model_Picture getWebshop_builder_3k_model_picture() {
        return webshop_builder_3k_model_picture;
    }

    public void setWebshop_builder_3k_model_picture(webshop_builder_3k_model_Picture webshop_builder_3k_model_picture) {
        this.webshop_builder_3k_model_picture = webshop_builder_3k_model_picture;
    }

}