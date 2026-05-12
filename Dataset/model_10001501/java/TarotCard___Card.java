





import java.util.List;
import java.util.ArrayList;

public class TarotCard___Card  {

    private int _id;
    private String _fortunes;
    private String _fileName;



    public TarotCard___Card(
        int _id,        String _fortunes,        String _fileName    ) {
        this._id = _id;
        this._fortunes = _fortunes;
        this._fileName = _fileName;
    }


    public int get_id() {
        return _id;
    }

    public void set_id(int _id) {
        this._id = _id;
    }
    public String get_fortunes() {
        return _fortunes;
    }

    public void set_fortunes(String _fortunes) {
        this._fortunes = _fortunes;
    }
    public String get_filename() {
        return _fileName;
    }

    public void set_filename(String _fileName) {
        this._fileName = _fileName;
    }


}