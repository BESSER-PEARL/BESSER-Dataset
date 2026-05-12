





import java.util.List;
import java.util.ArrayList;

public class Card  {






    private List<_unnamed> _unnameds;


    public Card(
    ) {
        this._unnameds = new ArrayList<>();
    }

    public Card(
        ArrayList<_unnamed> _unnameds    ) {
        this._unnameds = _unnameds;
    }


    public List<_unnamed> get_unnameds() {
        return _unnameds;
    }

    public void add_unnamed(_unnamed _unnamed) {
        this._unnameds.add(_unnamed);
    }

}