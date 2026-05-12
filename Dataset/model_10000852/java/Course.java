





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String CTutor;
    private String Cname;
    private String Cprice;
    private String Course_REG;
    private String Course_File_Name;
    private String Cid;



    public Course(
        String CTutor,        String Cname,        String Cprice,        String Course_REG,        String Course_File_Name,        String Cid    ) {
        this.CTutor = CTutor;
        this.Cname = Cname;
        this.Cprice = Cprice;
        this.Course_REG = Course_REG;
        this.Course_File_Name = Course_File_Name;
        this.Cid = Cid;
    }


    public String getCtutor() {
        return CTutor;
    }

    public void setCtutor(String CTutor) {
        this.CTutor = CTutor;
    }
    public String getCname() {
        return Cname;
    }

    public void setCname(String Cname) {
        this.Cname = Cname;
    }
    public String getCprice() {
        return Cprice;
    }

    public void setCprice(String Cprice) {
        this.Cprice = Cprice;
    }
    public String getCourse_reg() {
        return Course_REG;
    }

    public void setCourse_reg(String Course_REG) {
        this.Course_REG = Course_REG;
    }
    public String getCourse_file_name() {
        return Course_File_Name;
    }

    public void setCourse_file_name(String Course_File_Name) {
        this.Course_File_Name = Course_File_Name;
    }
    public String getCid() {
        return Cid;
    }

    public void setCid(String Cid) {
        this.Cid = Cid;
    }


}