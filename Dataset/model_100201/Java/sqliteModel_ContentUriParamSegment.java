





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ContentUriParamSegment extends ContentUriSegment {

    private boolean text;
    private boolean num;



    public sqliteModel_ContentUriParamSegment(
        boolean text,        boolean num    ) {
        super(
        );
        this.text = text;
        this.num = num;
    }


    public boolean getText() {
        return text;
    }

    public void setText(boolean text) {
        this.text = text;
    }
    public boolean getNum() {
        return num;
    }

    public void setNum(boolean num) {
        this.num = num;
    }


}