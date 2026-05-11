





import java.util.List;
import java.util.ArrayList;

public class iso20022_Doclet extends ModelEntity {

    private String type;
    private String content;



    public iso20022_Doclet(
        String type,        String content    ) {
        super(
        );
        this.type = type;
        this.content = content;
    }


    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }
    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}