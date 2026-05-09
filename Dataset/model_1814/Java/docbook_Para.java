





import java.util.List;
import java.util.ArrayList;

public class docbook_Para extends Identifiable {

    private String content;



    public docbook_Para(
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