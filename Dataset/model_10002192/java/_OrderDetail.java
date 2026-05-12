




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class _OrderDetail  {

    private int _productid;
    private int _totalamount;
    private int _quantity;
    private int _userid;
    private int OrderId;
    private int paymentInfoId;
    private LocalDate _orderdate;





    private Card card;




    private List<_Fee> _fees;


    public _OrderDetail(
        int _productid,        int _totalamount,        int _quantity,        int _userid,        int OrderId,        int paymentInfoId,        LocalDate _orderdate    ) {
        this._productid = _productid;
        this._totalamount = _totalamount;
        this._quantity = _quantity;
        this._userid = _userid;
        this.OrderId = OrderId;
        this.paymentInfoId = paymentInfoId;
        this._orderdate = _orderdate;
        this._fees = new ArrayList<>();
    }

    public _OrderDetail(
        int _productid,        int _totalamount,        int _quantity,        int _userid,        int OrderId,        int paymentInfoId,        LocalDate _orderdate        ArrayList<_Fee> _fees    ) {
        this._productid = _productid;
        this._totalamount = _totalamount;
        this._quantity = _quantity;
        this._userid = _userid;
        this.OrderId = OrderId;
        this.paymentInfoId = paymentInfoId;
        this._orderdate = _orderdate;
        this._fees = _fees;
    }

    public int get_productid() {
        return _productid;
    }

    public void set_productid(int _productid) {
        this._productid = _productid;
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
    public int get_userid() {
        return _userid;
    }

    public void set_userid(int _userid) {
        this._userid = _userid;
    }
    public int getOrderid() {
        return OrderId;
    }

    public void setOrderid(int OrderId) {
        this.OrderId = OrderId;
    }
    public int getPaymentinfoid() {
        return paymentInfoId;
    }

    public void setPaymentinfoid(int paymentInfoId) {
        this.paymentInfoId = paymentInfoId;
    }
    public LocalDate get_orderdate() {
        return _orderdate;
    }

    public void set_orderdate(LocalDate _orderdate) {
        this._orderdate = _orderdate;
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