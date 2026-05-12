





import java.util.List;
import java.util.ArrayList;

public class _TransactionType  {

    private String _type;





    private Card card;




    private List<_Fee> _fees;


    public _TransactionType(
        String _type    ) {
        this._type = _type;
        this._fees = new ArrayList<>();
    }

    public _TransactionType(
        String _type        ArrayList<_Fee> _fees    ) {
        this._type = _type;
        this._fees = _fees;
    }

    public String get_type() {
        return _type;
    }

    public void set_type(String _type) {
        this._type = _type;
    }

    public Card getCard() {
        return card;
    }

    public void setCard(Card card) {
        this.card = card;
    }
    public List<_Fee> get_fees() {
        return _fees;
    }

    public void add_fee(_fee _fee) {
        this._fees.add(_fee);
    }

}