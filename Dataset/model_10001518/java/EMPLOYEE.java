





import java.util.List;
import java.util.ArrayList;

public class EMPLOYEE  {

    private int EMP_ID;
    private String EMAIL_ID;
    private String QULIFICATION;
    private int CONTACT_NO;
    private String NAME;





    private ADMIN admin;


    public EMPLOYEE(
        int EMP_ID,        String EMAIL_ID,        String QULIFICATION,        int CONTACT_NO,        String NAME    ) {
        this.EMP_ID = EMP_ID;
        this.EMAIL_ID = EMAIL_ID;
        this.QULIFICATION = QULIFICATION;
        this.CONTACT_NO = CONTACT_NO;
        this.NAME = NAME;
    }


    public int getEmp_id() {
        return EMP_ID;
    }

    public void setEmp_id(int EMP_ID) {
        this.EMP_ID = EMP_ID;
    }
    public String getEmail_id() {
        return EMAIL_ID;
    }

    public void setEmail_id(String EMAIL_ID) {
        this.EMAIL_ID = EMAIL_ID;
    }
    public String getQulification() {
        return QULIFICATION;
    }

    public void setQulification(String QULIFICATION) {
        this.QULIFICATION = QULIFICATION;
    }
    public int getContact_no() {
        return CONTACT_NO;
    }

    public void setContact_no(int CONTACT_NO) {
        this.CONTACT_NO = CONTACT_NO;
    }
    public String getName() {
        return NAME;
    }

    public void setName(String NAME) {
        this.NAME = NAME;
    }

    public ADMIN getAdmin() {
        return admin;
    }

    public void setAdmin(ADMIN admin) {
        this.admin = admin;
    }

}