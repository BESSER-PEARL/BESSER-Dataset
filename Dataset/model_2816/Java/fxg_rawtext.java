





import java.util.List;
import java.util.ArrayList;

public class fxg_rawtext extends RichTextContent {

    private String _text;



    public fxg_rawtext(
        String _text    ) {
        super(
        );
        this._text = _text;
    }


    public String get_text() {
        return _text;
    }

    public void set_text(String _text) {
        this._text = _text;
    }


}