





import java.util.List;
import java.util.ArrayList;

public class frontend_core_PropertyWrite extends Expression {

    private String _property;



    public frontend_core_PropertyWrite(
        String _property    ) {
        super(
        );
        this._property = _property;
    }


    public String get_property() {
        return _property;
    }

    public void set_property(String _property) {
        this._property = _property;
    }


}