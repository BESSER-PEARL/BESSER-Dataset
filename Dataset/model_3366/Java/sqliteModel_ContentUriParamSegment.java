





import java.util.List;
import java.util.ArrayList;

public class sqliteModel_ContentUriParamSegment extends ContentUriSegment {

    private boolean num;
    private boolean text;



    public sqliteModel_ContentUriParamSegment(
        boolean num,        boolean text    ) {
        super(
        );
        this.num = num;
        this.text = text;
    }


    public boolean getNum() {
        return num;
    }

    public void setNum(boolean num) {
        this.num = num;
    }
    public boolean getText() {
        return text;
    }

    public void setText(boolean text) {
        this.text = text;
    }


}