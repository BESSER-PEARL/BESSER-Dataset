





import java.util.List;
import java.util.ArrayList;

public class webapp_Text extends Instruction {

    private String content;



    public webapp_Text(
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