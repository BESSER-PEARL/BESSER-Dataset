





import java.util.List;
import java.util.ArrayList;

public class Department  {

    private String CS;
    private String CSSE;
    private String ITM;
    private String JUR;
    private String MCM;
    private String IS;





    private Students students;


    public Department(
        String CS,        String CSSE,        String ITM,        String JUR,        String MCM,        String IS    ) {
        this.CS = CS;
        this.CSSE = CSSE;
        this.ITM = ITM;
        this.JUR = JUR;
        this.MCM = MCM;
        this.IS = IS;
    }


    public String getCs() {
        return CS;
    }

    public void setCs(String CS) {
        this.CS = CS;
    }
    public String getCsse() {
        return CSSE;
    }

    public void setCsse(String CSSE) {
        this.CSSE = CSSE;
    }
    public String getItm() {
        return ITM;
    }

    public void setItm(String ITM) {
        this.ITM = ITM;
    }
    public String getJur() {
        return JUR;
    }

    public void setJur(String JUR) {
        this.JUR = JUR;
    }
    public String getMcm() {
        return MCM;
    }

    public void setMcm(String MCM) {
        this.MCM = MCM;
    }
    public String getIs() {
        return IS;
    }

    public void setIs(String IS) {
        this.IS = IS;
    }

    public Students getStudents() {
        return students;
    }

    public void setStudents(Students students) {
        this.students = students;
    }

}