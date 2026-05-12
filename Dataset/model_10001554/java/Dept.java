





import java.util.List;
import java.util.ArrayList;

public class Dept  {

    private int DocId;
    private int Id;
    private String Name;



    public Dept(
        int DocId,        int Id,        String Name    ) {
        this.DocId = DocId;
        this.Id = Id;
        this.Name = Name;
    }


    public int getDocid() {
        return DocId;
    }

    public void setDocid(int DocId) {
        this.DocId = DocId;
    }
    public int getId() {
        return Id;
    }

    public void setId(int Id) {
        this.Id = Id;
    }
    public String getName() {
        return Name;
    }

    public void setName(String Name) {
        this.Name = Name;
    }


}