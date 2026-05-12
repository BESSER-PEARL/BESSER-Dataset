





import java.util.List;
import java.util.ArrayList;

public class _Product  {

    private int _producttypeid;
    private String _name;
    private int _price;
    private String _description;
    private int _stock;



    public _Product(
        int _producttypeid,        String _name,        int _price,        String _description,        int _stock    ) {
        this._producttypeid = _producttypeid;
        this._name = _name;
        this._price = _price;
        this._description = _description;
        this._stock = _stock;
    }


    public int get_producttypeid() {
        return _producttypeid;
    }

    public void set_producttypeid(int _producttypeid) {
        this._producttypeid = _producttypeid;
    }
    public String get_name() {
        return _name;
    }

    public void set_name(String _name) {
        this._name = _name;
    }
    public int get_price() {
        return _price;
    }

    public void set_price(int _price) {
        this._price = _price;
    }
    public String get_description() {
        return _description;
    }

    public void set_description(String _description) {
        this._description = _description;
    }
    public int get_stock() {
        return _stock;
    }

    public void set_stock(int _stock) {
        this._stock = _stock;
    }


}