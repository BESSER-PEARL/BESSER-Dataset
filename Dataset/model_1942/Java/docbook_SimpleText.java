





import java.util.List;
import java.util.ArrayList;

public class docbook_SimpleText extends ParaMixedContent {

    private String data;



    public docbook_SimpleText(
        String data    ) {
        super(
        );
        this.data = data;
    }


    public String getData() {
        return data;
    }

    public void setData(String data) {
        this.data = data;
    }


}