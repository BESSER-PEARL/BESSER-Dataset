





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private String toString;
    private int _CardSuit;
    private int Value;



    public Card(
        String toString,        int _CardSuit,        int Value    ) {
        this.toString = toString;
        this._CardSuit = _CardSuit;
        this.Value = Value;
    }


    public String getTostring() {
        return toString;
    }

    public void setTostring(String toString) {
        this.toString = toString;
    }
    public int get_cardsuit() {
        return _CardSuit;
    }

    public void set_cardsuit(int _CardSuit) {
        this._CardSuit = _CardSuit;
    }
    public int getValue() {
        return Value;
    }

    public void setValue(int Value) {
        this.Value = Value;
    }


}