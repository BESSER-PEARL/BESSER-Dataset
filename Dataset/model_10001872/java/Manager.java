





import java.util.List;
import java.util.ArrayList;

public class Manager  {

    private int managerID;
    private int phoneNo;
    private String name;
    private String branch;



    public Manager(
        int managerID,        int phoneNo,        String name,        String branch    ) {
        this.managerID = managerID;
        this.phoneNo = phoneNo;
        this.name = name;
        this.branch = branch;
    }


    public int getManagerid() {
        return managerID;
    }

    public void setManagerid(int managerID) {
        this.managerID = managerID;
    }
    public int getPhoneno() {
        return phoneNo;
    }

    public void setPhoneno(int phoneNo) {
        this.phoneNo = phoneNo;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBranch() {
        return branch;
    }

    public void setBranch(String branch) {
        this.branch = branch;
    }


}