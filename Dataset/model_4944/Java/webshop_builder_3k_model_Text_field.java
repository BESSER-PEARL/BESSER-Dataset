





import java.util.List;
import java.util.ArrayList;

public class webshop_builder_3k_model_Text_field extends Component {

    private String text;
    private int header_level;



    public webshop_builder_3k_model_Text_field(
        String text,        int header_level    ) {
        super(
        );
        this.text = text;
        this.header_level = header_level;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }
    public int getHeader_level() {
        return header_level;
    }

    public void setHeader_level(int header_level) {
        this.header_level = header_level;
    }


}