





import java.util.List;
import java.util.ArrayList;

public class becontent_Skinlet extends ViewItem {

    private String _id_model;
    private String template;



    public becontent_Skinlet(
        String _id_model,        String template    ) {
        super(
        );
        this._id_model = _id_model;
        this.template = template;
    }


    public String get_id_model() {
        return _id_model;
    }

    public void set_id_model(String _id_model) {
        this._id_model = _id_model;
    }
    public String getTemplate() {
        return template;
    }

    public void setTemplate(String template) {
        this.template = template;
    }


}