





import java.util.List;
import java.util.ArrayList;

public class Receptionist  {

    private String name;
    private int rID;
    private String branch;
    private int phoneNo;



    public Receptionist(
        String name,        int rID,        String branch,        int phoneNo    ) {
        this.name = name;
        this.rID = rID;
        this.branch = branch;
        this.phoneNo = phoneNo;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public int getRid() {
        return rID;
    }

    public void setRid(int rID) {
        this.rID = rID;
    }
    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }
    public int getPhoneno() {
        return phoneNo;
    }

    public void setPhoneno(int phoneNo) {
        this.phoneNo = phoneNo;
    }


}