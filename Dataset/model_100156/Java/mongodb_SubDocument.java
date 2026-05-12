





import java.util.List;
import java.util.ArrayList;

public class mongodb_SubDocument extends IValue {






    private List<mongodb_Field> mongodb_fields;


    public mongodb_SubDocument(
    ) {
        super(
        );
        this.mongodb_fields = new ArrayList<>();
    }

    public mongodb_SubDocument(
        ArrayList<mongodb_Field> mongodb_fields    ) {
        this.mongodb_fields = mongodb_fields;
    }


    public List<mongodb_Field> getMongodb_fields() {
        return mongodb_fields;
    }

    public void addMongodb_field(Mongodb_field mongodb_field) {
        this.mongodb_fields.add(mongodb_field);
    }

}