





import java.util.List;
import java.util.ArrayList;

public class iec61131_pous_Other_Language extends pous_Function_Block_Body, pous_Function_Body {

    private String text;



    public iec61131_pous_Other_Language(
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