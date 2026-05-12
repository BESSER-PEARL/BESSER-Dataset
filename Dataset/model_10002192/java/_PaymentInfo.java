




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class _PaymentInfo  {

    private LocalDate _expirydate;
    private int _cardno;
    private String _cardname;
    private int _cvv;
    private int paymentId;
    private int _userid;





    private _OrderDetail _orderdetail;


    public _PaymentInfo(
        LocalDate _expirydate,        int _cardno,        String _cardname,        int _cvv,        int paymentId,        int _userid    ) {
        this._expirydate = _expirydate;
        this._cardno = _cardno;
        this._cardname = _cardname;
        this._cvv = _cvv;
        this.paymentId = paymentId;
        this._userid = _userid;
    }


    public LocalDate get_expirydate() {
        return _expirydate;
    }

    public void set_expirydate(LocalDate _expirydate) {
        this._expirydate = _expirydate;
    }
    public int get_cardno() {
        return _cardno;
    }

    public void set_cardno(int _cardno) {
        this._cardno = _cardno;
    }
    public String get_cardname() {
        return _cardname;
    }

    public void set_cardname(String _cardname) {
        this._cardname = _cardname;
    }
    public int get_cvv() {
        return _cvv;
    }

    public void set_cvv(int _cvv) {
        this._cvv = _cvv;
    }
    public int getPaymentid() {
        return paymentId;
    }

    public void setPaymentid(int paymentId) {
        this.paymentId = paymentId;
    }
    public int get_userid() {
        return _userid;
    }

    public void set_userid(int _userid) {
        this._userid = _userid;
    }

    public _OrderDetail get_orderdetail() {
        return _orderdetail;
    }

    public void set_orderdetail(_OrderDetail _orderdetail) {
        this._orderdetail = _orderdetail;
    }

}