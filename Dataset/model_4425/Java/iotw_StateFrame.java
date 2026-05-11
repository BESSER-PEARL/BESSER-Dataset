





import java.util.List;
import java.util.ArrayList;

public class iotw_StateFrame extends StateControl {

    private String content;



    public iotw_StateFrame(
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