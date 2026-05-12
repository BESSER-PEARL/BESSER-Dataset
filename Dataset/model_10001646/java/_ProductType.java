





import java.util.List;
import java.util.ArrayList;

public class _ProductType  {

    private String _type;





    private List<_Product> _products;


    public _ProductType(
        String _type    ) {
        this._type = _type;
        this._products = new ArrayList<>();
    }

    public _ProductType(
        String _type        ArrayList<_Product> _products    ) {
        this._type = _type;
        this._products = _products;
    }

    public String get_type() {
        return _type;
    }

    public void set_type(String _type) {
        this._type = _type;
    }

    public List<_Product> get_products() {
        return _products;
    }

    public void add_product(_product _product) {
        this._products.add(_product);
    }

}