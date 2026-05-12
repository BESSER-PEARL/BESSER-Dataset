





import java.util.List;
import java.util.ArrayList;

public class Departmnt  {

    private String name;
    private int docid;
    private int id;



    public Departmnt(
        String name,        int docid,        int id    ) {
        this.name = name;
        this.docid = docid;
        this.id = id;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getDocid() {
        return docid;
    }

    public void setDocid(int docid) {
        this.docid = docid;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }


}