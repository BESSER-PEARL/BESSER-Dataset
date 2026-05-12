





import java.util.List;
import java.util.ArrayList;

public class _Fee  {

    private String _description;
    private int _price;
    private int _producttypeid;
    private int _stock;
    private String _name;



    public _Fee(
        String _description,        int _price,        int _producttypeid,        int _stock,        String _name    ) {
        this._description = _description;
        this._price = _price;
        this._producttypeid = _producttypeid;
        this._stock = _stock;
        this._name = _name;
    }


    public String get_description() {
        return _description;
    }

    public void set_description(String _description) {
        this._description = _description;
    }
    public int get_price() {
        return _price;
    }

    public void set_price(int _price) {
        this._price = _price;
    }
    public int get_producttypeid() {
        return _producttypeid;
    }

    public void set_producttypeid(int _producttypeid) {
        this._producttypeid = _producttypeid;
    }
    public int get_stock() {
        return _stock;
    }

    public void set_stock(int _stock) {
        this._stock = _stock;
    }
    public String get_name() {
        return _name;
    }

    public void set_name(String _name) {
        this._name = _name;
    }


}