





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Text_field extends Component {

    private int header_level;
    private String text;





    private webshop_builder_3k_model_Item webshop_builder_3k_model_item;




    private webshop_builder_3k_model_Branding webshop_builder_3k_model_branding;




    private webshop_builder_3k_model_Navigation_button webshop_builder_3k_model_navigation_button;


    public webshop_builder_3k_model_Text_field(
        int header_level,        String text    ) {
        super(
        );
        this.header_level = header_level;
        this.text = text;
    }


    public int getHeader_level() {
        return header_level;
    }

    public void setHeader_level(int header_level) {
        this.header_level = header_level;
    }
    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }

    public webshop_builder_3k_model_Item getWebshop_builder_3k_model_item() {
        return webshop_builder_3k_model_item;
    }

    public void setWebshop_builder_3k_model_item(webshop_builder_3k_model_Item webshop_builder_3k_model_item) {
        this.webshop_builder_3k_model_item = webshop_builder_3k_model_item;
    }
    public webshop_builder_3k_model_Branding getWebshop_builder_3k_model_branding() {
        return webshop_builder_3k_model_branding;
    }

    public void setWebshop_builder_3k_model_branding(webshop_builder_3k_model_Branding webshop_builder_3k_model_branding) {
        this.webshop_builder_3k_model_branding = webshop_builder_3k_model_branding;
    }
    public webshop_builder_3k_model_Navigation_button getWebshop_builder_3k_model_navigation_button() {
        return webshop_builder_3k_model_navigation_button;
    }

    public void setWebshop_builder_3k_model_navigation_button(webshop_builder_3k_model_Navigation_button webshop_builder_3k_model_navigation_button) {
        this.webshop_builder_3k_model_navigation_button = webshop_builder_3k_model_navigation_button;
    }

}