





import java.util.List;
import java.util.ArrayList;

public class mongodb_Document  {

    private String _id;





    private List<mongodb_Field> mongodb_fields;




    private mongodb_Collection mongodb_collection;


    public mongodb_Document(
        String _id    ) {
        this._id = _id;
        this.mongodb_fields = new ArrayList<>();
    }

    public mongodb_Document(
        String _id        ArrayList<mongodb_Field> mongodb_fields    ) {
        this._id = _id;
        this.mongodb_fields = mongodb_fields;
    }

    public String get_id() {
        return _id;
    }

    public void set_id(String _id) {
        this._id = _id;
    }

    public List<mongodb_Field> getMongodb_fields() {
        return mongodb_fields;
    }

    public void addMongodb_field(Mongodb_field mongodb_field) {
        this.mongodb_fields.add(mongodb_field);
    }
    public mongodb_Collection getMongodb_collection() {
        return mongodb_collection;
    }

    public void setMongodb_collection(mongodb_Collection mongodb_collection) {
        this.mongodb_collection = mongodb_collection;
    }

}