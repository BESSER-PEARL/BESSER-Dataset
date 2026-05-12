





import java.util.List;
import java.util.ArrayList;

public class library  {

    private String _location;
    private String _librarion_id;



    public library(
        String _location,        String _librarion_id    ) {
        this._location = _location;
        this._librarion_id = _librarion_id;
    }


    public String get_location() {
        return _location;
    }

    public void set_location(String _location) {
        this._location = _location;
    }
    public String get_librarion_id() {
        return _librarion_id;
    }

    public void set_librarion_id(String _librarion_id) {
        this._librarion_id = _librarion_id;
    }


}