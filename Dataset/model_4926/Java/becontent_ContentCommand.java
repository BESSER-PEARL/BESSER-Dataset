





import java.util.List;
import java.util.ArrayList;

public class becontent_ContentCommand  {

    private String _id_model;





    private becontent_Content becontent_content;


    public becontent_ContentCommand(
        String _id_model    ) {
        this._id_model = _id_model;
    }


    public String get_id_model() {
        return _id_model;
    }

    public void set_id_model(String _id_model) {
        this._id_model = _id_model;
    }

    public becontent_Content getBecontent_content() {
        return becontent_content;
    }

    public void setBecontent_content(becontent_Content becontent_content) {
        this.becontent_content = becontent_content;
    }

}