




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class _PaymentInfo  {

    private int _userid;
    private int paymentId;
    private int _cardno;
    private int _cvv;
    private String _cardname;
    private LocalDate _expirydate;





    private _OrderDetail _orderdetail;


    public _PaymentInfo(
        int _userid,        int paymentId,        int _cardno,        int _cvv,        String _cardname,        LocalDate _expirydate    ) {
        this._userid = _userid;
        this.paymentId = paymentId;
        this._cardno = _cardno;
        this._cvv = _cvv;
        this._cardname = _cardname;
        this._expirydate = _expirydate;
    }


    public int get_userid() {
        return _userid;
    }

    public void set_userid(int _userid) {
        this._userid = _userid;
    }
    public int getPaymentid() {
        return paymentId;
    }

    public void setPaymentid(int paymentId) {
        this.paymentId = paymentId;
    }
    public int get_cardno() {
        return _cardno;
    }

    public void set_cardno(int _cardno) {
        this._cardno = _cardno;
    }
    public int get_cvv() {
        return _cvv;
    }

    public void set_cvv(int _cvv) {
        this._cvv = _cvv;
    }
    public String get_cardname() {
        return _cardname;
    }

    public void set_cardname(String _cardname) {
        this._cardname = _cardname;
    }
    public LocalDate get_expirydate() {
        return _expirydate;
    }

    public void set_expirydate(LocalDate _expirydate) {
        this._expirydate = _expirydate;
    }

    public _OrderDetail get_orderdetail() {
        return _orderdetail;
    }

    public void set_orderdetail(_OrderDetail _orderdetail) {
        this._orderdetail = _orderdetail;
    }

}