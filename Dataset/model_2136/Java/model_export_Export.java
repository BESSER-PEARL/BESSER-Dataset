





import java.util.List;
import java.util.ArrayList;

public class model_export_Export extends INamed {

    private String content;
    private String type;



    public model_export_Export(
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