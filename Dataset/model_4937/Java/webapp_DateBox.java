





import java.util.List;
import java.util.ArrayList;

public class webapp_DateBox extends TextBox {

    private String format;



    public webapp_DateBox(
        String format    ) {
        super(
        );
        this.format = format;
    }


    public String getFormat() {
        return format;
    }

    public void setFormat(String format) {
        this.format = format;
    }


}