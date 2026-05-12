





import java.util.List;
import java.util.ArrayList;

public class _LoginCredential  {

    private String _loginid;
    private String _password;



    public _LoginCredential(
        String _loginid,        String _password    ) {
        this._loginid = _loginid;
        this._password = _password;
    }


    public String get_loginid() {
        return _loginid;
    }

    public void set_loginid(String _loginid) {
        this._loginid = _loginid;
    }
    public String get_password() {
        return _password;
    }

    public void set_password(String _password) {
        this._password = _password;
    }


}