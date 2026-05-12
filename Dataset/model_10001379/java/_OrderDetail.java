




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class _OrderDetail  {

    private int _totalamount;
    private int _quantity;
    private int OrderId;
    private int _productid;
    private int paymentInfoId;
    private int _userid;
    private LocalDate _orderdate;





    private List<_Product> _products;




    private Farmer farmer;


    public _OrderDetail(
        int _totalamount,        int _quantity,        int OrderId,        int _productid,        int paymentInfoId,        int _userid,        LocalDate _orderdate    ) {
        this._totalamount = _totalamount;
        this._quantity = _quantity;
        this.OrderId = OrderId;
        this._productid = _productid;
        this.paymentInfoId = paymentInfoId;
        this._userid = _userid;
        this._orderdate = _orderdate;
        this._products = new ArrayList<>();
    }

    public _OrderDetail(
        int _totalamount,        int _quantity,        int OrderId,        int _productid,        int paymentInfoId,        int _userid,        LocalDate _orderdate        ArrayList<_Product> _products    ) {
        this._totalamount = _totalamount;
        this._quantity = _quantity;
        this.OrderId = OrderId;
        this._productid = _productid;
        this.paymentInfoId = paymentInfoId;
        this._userid = _userid;
        this._orderdate = _orderdate;
        this._products = _products;
    }

    public int get_totalamount() {
        return _totalamount;
    }

    public void set_totalamount(int _totalamount) {
        this._totalamount = _totalamount;
    }
    public int get_quantity() {
        return _quantity;
    }

    public void set_quantity(int _quantity) {
        this._quantity = _quantity;
    }
    public int getOrderid() {
        return OrderId;
    }

    public void setOrderid(int OrderId) {
        this.OrderId = OrderId;
    }
    public int get_productid() {
        return _productid;
    }

    public void set_productid(int _productid) {
        this._productid = _productid;
    }
    public int getPaymentinfoid() {
        return paymentInfoId;
    }

    public void setPaymentinfoid(int paymentInfoId) {
        this.paymentInfoId = paymentInfoId;
    }
    public int get_userid() {
        return _userid;
    }

    public void set_userid(int _userid) {
        this._userid = _userid;
    }
    public LocalDate get_orderdate() {
        return _orderdate;
    }

    public void set_orderdate(LocalDate _orderdate) {
        this._orderdate = _orderdate;
    }

    public List<_Product> get_products() {
        return _products;
    }

    public void add_product(_product _product) {
        this._products.add(_product);
    }
    public Farmer getFarmer() {
        return farmer;
    }

    public void setFarmer(Farmer farmer) {
        this.farmer = farmer;
    }

}