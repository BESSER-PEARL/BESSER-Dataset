





import java.util.List;
import java.util.ArrayList;

public class mongodb_ValueList extends IValue {






    private List<mongodb_IValue> mongodb_ivalues;


    public mongodb_ValueList(
    ) {
        super(
        );
        this.mongodb_ivalues = new ArrayList<>();
    }

    public mongodb_ValueList(
        ArrayList<mongodb_IValue> mongodb_ivalues    ) {
        this.mongodb_ivalues = mongodb_ivalues;
    }


    public List<mongodb_IValue> getMongodb_ivalues() {
        return mongodb_ivalues;
    }

    public void addMongodb_ivalue(Mongodb_ivalue mongodb_ivalue) {
        this.mongodb_ivalues.add(mongodb_ivalue);
    }

}