





import java.util.List;
import java.util.ArrayList;

public class Dept  {

    private String DeptName;
    private int id;
    private int Docid;



    public Dept(
        String DeptName,        int id,        int Docid    ) {
        this.DeptName = DeptName;
        this.id = id;
        this.Docid = Docid;
    }


    public String getDeptname() {
        return DeptName;
    }

    public void setDeptname(String DeptName) {
        this.DeptName = DeptName;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public int getDocid() {
        return Docid;
    }

    public void setDocid(int Docid) {
        this.Docid = Docid;
    }


}