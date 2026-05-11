





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Picture extends Component {

    private String title;
    private String alternative_text;
    private String source;





    private webshop_builder_3k_model_Item webshop_builder_3k_model_item;




    private webshop_builder_3k_model_Branding webshop_builder_3k_model_branding;


    public webshop_builder_3k_model_Picture(
        String title,        String alternative_text,        String source    ) {
        super(
        );
        this.title = title;
        this.alternative_text = alternative_text;
        this.source = source;
    }


    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }
    public String getAlternative_text() {
        return alternative_text;
    }

    public void setAlternative_text(String alternative_text) {
        this.alternative_text = alternative_text;
    }
    public String getSource() {
        return source;
    }

    public void setSource(String source) {
        this.source = source;
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

}