





import java.util.List;
import java.util.ArrayList;

public class becontent_Template extends ViewItem {

    private String _id_model;
    private String path;



    public becontent_Template(
        String _id_model,        String path    ) {
        super(
        );
        this._id_model = _id_model;
        this.path = path;
    }


    public String get_id_model() {
        return _id_model;
    }

    public void set_id_model(String _id_model) {
        this._id_model = _id_model;
    }
    public String getPath() {
        return path;
    }

    public void setPath(String path) {
        this.path = path;
    }


}