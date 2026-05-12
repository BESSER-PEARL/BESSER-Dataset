





import java.util.List;
import java.util.ArrayList;

public class _ProductRating  {

    private int _userid;
    private int _productid;
    private int _rating;





    private List<_User> _users;


    public _ProductRating(
        int _userid,        int _productid,        int _rating    ) {
        this._userid = _userid;
        this._productid = _productid;
        this._rating = _rating;
        this._users = new ArrayList<>();
    }

    public _ProductRating(
        int _userid,        int _productid,        int _rating        ArrayList<_User> _users    ) {
        this._userid = _userid;
        this._productid = _productid;
        this._rating = _rating;
        this._users = _users;
    }

    public int get_userid() {
        return _userid;
    }

    public void set_userid(int _userid) {
        this._userid = _userid;
    }
    public int get_productid() {
        return _productid;
    }

    public void set_productid(int _productid) {
        this._productid = _productid;
    }
    public int get_rating() {
        return _rating;
    }

    public void set_rating(int _rating) {
        this._rating = _rating;
    }

    public List<_User> get_users() {
        return _users;
    }

    public void add_user(_user _user) {
        this._users.add(_user);
    }

}