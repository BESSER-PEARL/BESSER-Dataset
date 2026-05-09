





import java.util.List;
import java.util.ArrayList;

public class DBLP_Author  {

    private String name;





    private List<DBLP_Record> dblp_records;




    private DBLP_Record dblp_record;


    public DBLP_Author(
        String name    ) {
        this.name = name;
        this.dblp_records = new ArrayList<>();
    }

    public DBLP_Author(
        String name        ArrayList<DBLP_Record> dblp_records    ) {
        this.name = name;
        this.dblp_records = dblp_records;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<DBLP_Record> getDblp_records() {
        return dblp_records;
    }

    public void addDblp_record(Dblp_record dblp_record) {
        this.dblp_records.add(dblp_record);
    }
    public DBLP_Record getDblp_record() {
        return dblp_record;
    }

    public void setDblp_record(DBLP_Record dblp_record) {
        this.dblp_record = dblp_record;
    }

}