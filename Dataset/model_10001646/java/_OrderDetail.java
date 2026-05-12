




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class _OrderDetail  {

    private int _quantity;
    private int _userid;
    private int _totalamount;
    private int _productid;
    private LocalDate _orderdate;





    private _User _user;




    private List<_Product> _products;


    public _OrderDetail(
        int _quantity,        int _userid,        int _totalamount,        int _productid,        LocalDate _orderdate    ) {
        this._quantity = _quantity;
        this._userid = _userid;
        this._totalamount = _totalamount;
        this._productid = _productid;
        this._orderdate = _orderdate;
        this._products = new ArrayList<>();
    }

    public _OrderDetail(
        int _quantity,        int _userid,        int _totalamount,        int _productid,        LocalDate _orderdate        ArrayList<_Product> _products    ) {
        this._quantity = _quantity;
        this._userid = _userid;
        this._totalamount = _totalamount;
        this._productid = _productid;
        this._orderdate = _orderdate;
        this._products = _products;
    }

    public int get_quantity() {
        return _quantity;
    }

    public void set_quantity(int _quantity) {
        this._quantity = _quantity;
    }
    public int get_userid() {
        return _userid;
    }

    public void set_userid(int _userid) {
        this._userid = _userid;
    }
    public int get_totalamount() {
        return _totalamount;
    }

    public void set_totalamount(int _totalamount) {
        this._totalamount = _totalamount;
    }
    public int get_productid() {
        return _productid;
    }

    public void set_productid(int _productid) {
        this._productid = _productid;
    }
    public LocalDate get_orderdate() {
        return _orderdate;
    }

    public void set_orderdate(LocalDate _orderdate) {
        this._orderdate = _orderdate;
    }

    public _User get_user() {
        return _user;
    }

    public void set_user(_User _user) {
        this._user = _user;
    }
    public List<_Product> get_products() {
        return _products;
    }

    public void add_product(_product _product) {
        this._products.add(_product);
    }

}