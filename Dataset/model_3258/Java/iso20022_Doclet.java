





import java.util.List;
import java.util.ArrayList;

public class iso20022_Doclet extends ModelEntity {

    private String content;
    private String type;



    public iso20022_Doclet(
        String content,        String type    ) {
        super(
        );
        this.content = content;
        this.type = type;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }
    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }


}