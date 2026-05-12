





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int _Suit;
    private int _CardNumber;
    private int _CardValue;



    public Card(
        int _Suit,        int _CardNumber,        int _CardValue    ) {
        this._Suit = _Suit;
        this._CardNumber = _CardNumber;
        this._CardValue = _CardValue;
    }


    public int get_suit() {
        return _Suit;
    }

    public void set_suit(int _Suit) {
        this._Suit = _Suit;
    }
    public int get_cardnumber() {
        return _CardNumber;
    }

    public void set_cardnumber(int _CardNumber) {
        this._CardNumber = _CardNumber;
    }
    public int get_cardvalue() {
        return _CardValue;
    }

    public void set_cardvalue(int _CardValue) {
        this._CardValue = _CardValue;
    }


}