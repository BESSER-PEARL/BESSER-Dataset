





import java.util.List;
import java.util.ArrayList;

public class becontent_Validation  {

    private String _id_model;
    private String message;
    private String condition;



    public becontent_Validation(
        String _id_model,        String message,        String condition    ) {
        this._id_model = _id_model;
        this.message = message;
        this.condition = condition;
    }


    public String get_id_model() {
        return _id_model;
    }

    public void set_id_model(String _id_model) {
        this._id_model = _id_model;
    }
    public String getMessage() {
        return message;
    }

    public void setMessage(String message) {
        this.message = message;
    }
    public String getCondition() {
        return condition;
    }

    public void setCondition(String condition) {
        this.condition = condition;
    }


}