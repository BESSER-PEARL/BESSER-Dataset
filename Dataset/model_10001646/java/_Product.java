





import java.util.List;
import java.util.ArrayList;

public class _Product  {

    private String _description;
    private int _price;
    private String _name;
    private int _producttypeid;
    private String _modelno;
    private int _stock;





    private List<_ProductRating> _productratings;


    public _Product(
        String _description,        int _price,        String _name,        int _producttypeid,        String _modelno,        int _stock    ) {
        this._description = _description;
        this._price = _price;
        this._name = _name;
        this._producttypeid = _producttypeid;
        this._modelno = _modelno;
        this._stock = _stock;
        this._productratings = new ArrayList<>();
    }

    public _Product(
        String _description,        int _price,        String _name,        int _producttypeid,        String _modelno,        int _stock        ArrayList<_ProductRating> _productratings    ) {
        this._description = _description;
        this._price = _price;
        this._name = _name;
        this._producttypeid = _producttypeid;
        this._modelno = _modelno;
        this._stock = _stock;
        this._productratings = _productratings;
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
    public String get_name() {
        return _name;
    }

    public void set_name(String _name) {
        this._name = _name;
    }
    public int get_producttypeid() {
        return _producttypeid;
    }

    public void set_producttypeid(int _producttypeid) {
        this._producttypeid = _producttypeid;
    }
    public String get_modelno() {
        return _modelno;
    }

    public void set_modelno(String _modelno) {
        this._modelno = _modelno;
    }
    public int get_stock() {
        return _stock;
    }

    public void set_stock(int _stock) {
        this._stock = _stock;
    }

    public List<_ProductRating> get_productratings() {
        return _productratings;
    }

    public void add_productrating(_productrating _productrating) {
        this._productratings.add(_productrating);
    }

}