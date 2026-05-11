





import java.util.List;
import java.util.ArrayList;

public class dgf_DReference extends DVertex {

    private boolean _property;



    public dgf_DReference(
        boolean _property    ) {
        super(
        );
        this._property = _property;
    }


    public boolean get_property() {
        return _property;
    }

    public void set_property(boolean _property) {
        this._property = _property;
    }


}