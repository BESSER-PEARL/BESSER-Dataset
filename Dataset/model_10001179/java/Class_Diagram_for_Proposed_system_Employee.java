





import java.util.List;
import java.util.ArrayList;

public class Class_Diagram_for_Proposed_system_Employee  {

    private String gender;
    private int userId;
    private int id;
    private String mobile;
    private int postID;
    private int deptId;
    private String address;
    private String phone;
    private String NIC;
    private int shiftId;



    public Class_Diagram_for_Proposed_system_Employee(
        String gender,        int userId,        int id,        String mobile,        int postID,        int deptId,        String address,        String phone,        String NIC,        int shiftId    ) {
        this.gender = gender;
        this.userId = userId;
        this.id = id;
        this.mobile = mobile;
        this.postID = postID;
        this.deptId = deptId;
        this.address = address;
        this.phone = phone;
        this.NIC = NIC;
        this.shiftId = shiftId;
    }


    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public int getUserid() {
        return userId;
    }

    public void setUserid(int userId) {
        this.userId = userId;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getMobile() {
        return mobile;
    }

    public void setMobile(String mobile) {
        this.mobile = mobile;
    }
    public int getPostid() {
        return postID;
    }

    public void setPostid(int postID) {
        this.postID = postID;
    }
    public int getDeptid() {
        return deptId;
    }

    public void setDeptid(int deptId) {
        this.deptId = deptId;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getPhone() {
        return phone;
    }

    public void setPhone(String phone) {
        this.phone = phone;
    }
    public String getNic() {
        return NIC;
    }

    public void setNic(String NIC) {
        this.NIC = NIC;
    }
    public int getShiftid() {
        return shiftId;
    }

    public void setShiftid(int shiftId) {
        this.shiftId = shiftId;
    }


}