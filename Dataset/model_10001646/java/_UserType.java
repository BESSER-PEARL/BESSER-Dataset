





import java.util.List;
import java.util.ArrayList;

public class _UserType  {

    private String _userrole;





    private List<_User> _users;


    public _UserType(
        String _userrole    ) {
        this._userrole = _userrole;
        this._users = new ArrayList<>();
    }

    public _UserType(
        String _userrole        ArrayList<_User> _users    ) {
        this._userrole = _userrole;
        this._users = _users;
    }

    public String get_userrole() {
        return _userrole;
    }

    public void set_userrole(String _userrole) {
        this._userrole = _userrole;
    }

    public List<_User> get_users() {
        return _users;
    }

    public void add_user(_user _user) {
        this._users.add(_user);
    }

}