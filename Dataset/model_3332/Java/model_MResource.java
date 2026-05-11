





import java.util.List;
import java.util.ArrayList;

public class model_MResource extends AbstractMResource {

    private String content;



    public model_MResource(
        String content    ) {
        super(
        );
        this.content = content;
    }


    public String getContent() {
        return content;
    }

    public void setContent(String content) {
        this.content = content;
    }


}