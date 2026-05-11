





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Picture extends Component {

    private String alternative_text;
    private String source;
    private String title;



    public webshop_builder_3k_model_Picture(
        String alternative_text,        String source,        String title    ) {
        super(
        );
        this.alternative_text = alternative_text;
        this.source = source;
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
    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }


}