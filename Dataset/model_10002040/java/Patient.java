





import java.util.List;
import java.util.ArrayList;

public class Patient  {

    private String telno1;
    private String birth;
    private String gender;
    private String attribute;
    private String address;
    private String gender1;
    private String tcno;
    private String name;
    private String birth1;
    private String tcno1;
    private String address1;
    private String name1;
    private String telno;





    private Receptionist receptionist;


    public Patient(
        String telno1,        String birth,        String gender,        String attribute,        String address,        String gender1,        String tcno,        String name,        String birth1,        String tcno1,        String address1,        String name1,        String telno    ) {
        this.telno1 = telno1;
        this.birth = birth;
        this.gender = gender;
        this.attribute = attribute;
        this.address = address;
        this.gender1 = gender1;
        this.tcno = tcno;
        this.name = name;
        this.birth1 = birth1;
        this.tcno1 = tcno1;
        this.address1 = address1;
        this.name1 = name1;
        this.telno = telno;
    }


    public String getTelno1() {
        return telno1;
    }

    public void setTelno1(String telno1) {
        this.telno1 = telno1;
    }
    public String getBirth() {
        return birth;
    }

    public void setBirth(String birth) {
        this.birth = birth;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public String getGender1() {
        return gender1;
    }

    public void setGender1(String gender1) {
        this.gender1 = gender1;
    }
    public String getTcno() {
        return tcno;
    }

    public void setTcno(String tcno) {
        this.tcno = tcno;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getBirth1() {
        return birth1;
    }

    public void setBirth1(String birth1) {
        this.birth1 = birth1;
    }
    public String getTcno1() {
        return tcno1;
    }

    public void setTcno1(String tcno1) {
        this.tcno1 = tcno1;
    }
    public String getAddress1() {
        return address1;
    }

    public void setAddress1(String address1) {
        this.address1 = address1;
    }
    public String getName1() {
        return name1;
    }

    public void setName1(String name1) {
        this.name1 = name1;
    }
    public String getTelno() {
        return telno;
    }

    public void setTelno(String telno) {
        this.telno = telno;
    }

    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }

}