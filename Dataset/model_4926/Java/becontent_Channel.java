





import java.util.List;
import java.util.ArrayList;

public class becontent_Channel extends BeContentElement {

    private String _id_model;
    private String parameters;



    public becontent_Channel(
        String _id_model,        String parameters    ) {
        super(
        );
        this._id_model = _id_model;
        this.parameters = parameters;
    }


    public String get_id_model() {
        return _id_model;
    }

    public void set_id_model(String _id_model) {
        this._id_model = _id_model;
    }
    public String getParameters() {
        return parameters;
    }

    public void setParameters(String parameters) {
        this.parameters = parameters;
    }


}