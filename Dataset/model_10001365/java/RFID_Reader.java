




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class RFID_Reader  {

    private String address;
    private int phone;
    private String Gender;
    private LocalDate birthDate;
    private int RFID;
    private String CRC_code;



    public RFID_Reader(
        String address,        int phone,        String Gender,        LocalDate birthDate,        int RFID,        String CRC_code    ) {
        this.address = address;
        this.phone = phone;
        this.Gender = Gender;
        this.birthDate = birthDate;
        this.RFID = RFID;
        this.CRC_code = CRC_code;
    }


    public String getAddress() {
        return address;
    }

    public void setAddress(String address) {
        this.address = address;
    }
    public int getPhone() {
        return phone;
    }

    public void setPhone(int phone) {
        this.phone = phone;
    }
    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }
    public LocalDate getBirthdate() {
        return birthDate;
    }

    public void setBirthdate(LocalDate birthDate) {
        this.birthDate = birthDate;
    }
    public int getRfid() {
        return RFID;
    }

    public void setRfid(int RFID) {
        this.RFID = RFID;
    }
    public String getCrc_code() {
        return CRC_code;
    }

    public void setCrc_code(String CRC_code) {
        this.CRC_code = CRC_code;
    }


}