





import java.util.List;
import java.util.ArrayList;

public class Course  {

    private String Course_File_Name;
    private String Course_REG;
    private String Cprice;
    private String CTutor;
    private String Cid;
    private String Cname;



    public Course(
        String Course_File_Name,        String Course_REG,        String Cprice,        String CTutor,        String Cid,        String Cname    ) {
        this.Course_File_Name = Course_File_Name;
        this.Course_REG = Course_REG;
        this.Cprice = Cprice;
        this.CTutor = CTutor;
        this.Cid = Cid;
        this.Cname = Cname;
    }


    public String getCourse_file_name() {
        return Course_File_Name;
    }

    public void setCourse_file_name(String Course_File_Name) {
        this.Course_File_Name = Course_File_Name;
    }
    public String getCourse_reg() {
        return Course_REG;
    }

    public void setCourse_reg(String Course_REG) {
        this.Course_REG = Course_REG;
    }
    public String getCprice() {
        return Cprice;
    }

    public void setCprice(String Cprice) {
        this.Cprice = Cprice;
    }
    public String getCtutor() {
        return CTutor;
    }

    public void setCtutor(String CTutor) {
        this.CTutor = CTutor;
    }
    public String getCid() {
        return Cid;
    }

    public void setCid(String Cid) {
        this.Cid = Cid;
    }
    public String getCname() {
        return Cname;
    }

    public void setCname(String Cname) {
        this.Cname = Cname;
    }


}