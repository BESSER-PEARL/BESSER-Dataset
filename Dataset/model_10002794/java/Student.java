





import java.util.List;
import java.util.ArrayList;

public class Student  {

    private String reg_Num;
    private String name;
    private String mail_ID;



    public Student(
        String reg_Num,        String name,        String mail_ID    ) {
        this.reg_Num = reg_Num;
        this.name = name;
        this.mail_ID = mail_ID;
    }


    public String getReg_num() {
        return reg_Num;
    }

    public void setReg_num(String reg_Num) {
        this.reg_Num = reg_Num;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getMail_id() {
        return mail_ID;
    }

    public void setMail_id(String mail_ID) {
        this.mail_ID = mail_ID;
    }


}