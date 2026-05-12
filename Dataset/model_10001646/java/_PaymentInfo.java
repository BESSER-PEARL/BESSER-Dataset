




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class _PaymentInfo  {

    private String _cardname;
    private LocalDate _expirydate;
    private int _cardno;
    private int _cvv;
    private int _userid;





    private _User _user;


    public _PaymentInfo(
        String _cardname,        LocalDate _expirydate,        int _cardno,        int _cvv,        int _userid    ) {
        this._cardname = _cardname;
        this._expirydate = _expirydate;
        this._cardno = _cardno;
        this._cvv = _cvv;
        this._userid = _userid;
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
    public int get_userid() {
        return _userid;
    }

    public void set_userid(int _userid) {
        this._userid = _userid;
    }

    public _User get_user() {
        return _user;
    }

    public void set_user(_User _user) {
        this._user = _user;
    }

}