





import java.util.List;
import java.util.ArrayList;

public class Deck  {

    private int deckArray;
    private int size;





    private _Interface _interface;


    public Deck(
        int deckArray,        int size    ) {
        this.deckArray = deckArray;
        this.size = size;
    }


    public int getDeckarray() {
        return deckArray;
    }

    public void setDeckarray(int deckArray) {
        this.deckArray = deckArray;
    }
    public int getSize() {
        return size;
    }

    public void setSize(int size) {
        this.size = size;
    }

    public _Interface get_interface() {
        return _interface;
    }

    public void set_interface(_Interface _interface) {
        this._interface = _interface;
    }

}