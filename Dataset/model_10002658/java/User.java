





import java.util.List;
import java.util.ArrayList;

public class User  {

    private None _P;
    private None _F;
    private None __M;





    private HomePage homepage;




    private Message message;




    private Friend friend;




    private Photos photos;


    public User(
        None _P,        None _F,        None __M    ) {
        this._P = _P;
        this._F = _F;
        this.__M = __M;
    }


    public None get_p() {
        return _P;
    }

    public void set_p(None _P) {
        this._P = _P;
    }
    public None get_f() {
        return _F;
    }

    public void set_f(None _F) {
        this._F = _F;
    }
    public None get__m() {
        return __M;
    }

    public void set__m(None __M) {
        this.__M = __M;
    }

    public HomePage getHomepage() {
        return homepage;
    }

    public void setHomepage(HomePage homepage) {
        this.homepage = homepage;
    }
    public Message getMessage() {
        return message;
    }

    public void setMessage(Message message) {
        this.message = message;
    }
    public Friend getFriend() {
        return friend;
    }

    public void setFriend(Friend friend) {
        this.friend = friend;
    }
    public Photos getPhotos() {
        return photos;
    }

    public void setPhotos(Photos photos) {
        this.photos = photos;
    }

}