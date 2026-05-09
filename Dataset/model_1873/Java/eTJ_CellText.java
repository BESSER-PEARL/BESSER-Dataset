





import java.util.List;
import java.util.ArrayList;

public class eTJ_CellText extends ColumnAttribute {

    private String text;



    public eTJ_CellText(
        String text    ) {
        super(
        );
        this.text = text;
    }


    public String getText() {
        return text;
    }

    public void setText(String text) {
        this.text = text;
    }


}