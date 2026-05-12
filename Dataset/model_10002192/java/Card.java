





import java.util.List;
import java.util.ArrayList;

public class Card  {

    private int _usertypeid;
    private String _username;
    private int _phone;
    private int _logincredentialsid;
    private String _email;
    private String _address;





    private _LoginCredential _logincredential;


    public Card(
        int _usertypeid,        String _username,        int _phone,        int _logincredentialsid,        String _email,        String _address    ) {
        this._usertypeid = _usertypeid;
        this._username = _username;
        this._phone = _phone;
        this._logincredentialsid = _logincredentialsid;
        this._email = _email;
        this._address = _address;
    }


    public int get_usertypeid() {
        return _usertypeid;
    }

    public void set_usertypeid(int _usertypeid) {
        this._usertypeid = _usertypeid;
    }
    public String get_username() {
        return _username;
    }

    public void set_username(String _username) {
        this._username = _username;
    }
    public int get_phone() {
        return _phone;
    }

    public void set_phone(int _phone) {
        this._phone = _phone;
    }
    public int get_logincredentialsid() {
        return _logincredentialsid;
    }

    public void set_logincredentialsid(int _logincredentialsid) {
        this._logincredentialsid = _logincredentialsid;
    }
    public String get_email() {
        return _email;
    }

    public void set_email(String _email) {
        this._email = _email;
    }
    public String get_address() {
        return _address;
    }

    public void set_address(String _address) {
        this._address = _address;
    }

    public _LoginCredential get_logincredential() {
        return _logincredential;
    }

    public void set_logincredential(_LoginCredential _logincredential) {
        this._logincredential = _logincredential;
    }

}