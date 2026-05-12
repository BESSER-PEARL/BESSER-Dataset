





import java.util.List;
import java.util.ArrayList;

public class Personel  {

    private String registerno;
    private String attribute7;
    private String gender;
    private String tcno;
    private String attribute;
    private String corporation;
    private String name1;
    private String position;
    private String name;
    private String tcno1;





    private Receptionist receptionist;




    private Receptionist receptionist;




    private Patient patient;




    private Patient patient;


    public Personel(
        String registerno,        String attribute7,        String gender,        String tcno,        String attribute,        String corporation,        String name1,        String position,        String name,        String tcno1    ) {
        this.registerno = registerno;
        this.attribute7 = attribute7;
        this.gender = gender;
        this.tcno = tcno;
        this.attribute = attribute;
        this.corporation = corporation;
        this.name1 = name1;
        this.position = position;
        this.name = name;
        this.tcno1 = tcno1;
    }


    public String getRegisterno() {
        return registerno;
    }

    public void setRegisterno(String registerno) {
        this.registerno = registerno;
    }
    public String getAttribute7() {
        return attribute7;
    }

    public void setAttribute7(String attribute7) {
        this.attribute7 = attribute7;
    }
    public String getGender() {
        return gender;
    }

    public void setGender(String gender) {
        this.gender = gender;
    }
    public String getTcno() {
        return tcno;
    }

    public void setTcno(String tcno) {
        this.tcno = tcno;
    }
    public String getAttribute() {
        return attribute;
    }

    public void setAttribute(String attribute) {
        this.attribute = attribute;
    }
    public String getCorporation() {
        return corporation;
    }

    public void setCorporation(String corporation) {
        this.corporation = corporation;
    }
    public String getName1() {
        return name1;
    }

    public void setName1(String name1) {
        this.name1 = name1;
    }
    public String getPosition() {
        return position;
    }

    public void setPosition(String position) {
        this.position = position;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTcno1() {
        return tcno1;
    }

    public void setTcno1(String tcno1) {
        this.tcno1 = tcno1;
    }

    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }
    public Receptionist getReceptionist() {
        return receptionist;
    }

    public void setReceptionist(Receptionist receptionist) {
        this.receptionist = receptionist;
    }
    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }
    public Patient getPatient() {
        return patient;
    }

    public void setPatient(Patient patient) {
        this.patient = patient;
    }

}