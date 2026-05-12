





import java.util.List;
import java.util.ArrayList;

public class Users  {

    private String universityStructureUnit;
    private String residentPassword;
    private String residentSurname;
    private String residentPosition;
    private String residentBirthday;
    private int individuadIdentificationCode;
    private String residentName;
    private String residentEmail;
    private int registrationCertificateCode;
    private String residentDepartment;
    private String residentPatronymic;
    private int id;
    private String residentUserType;



    public Users(
        String universityStructureUnit,        String residentPassword,        String residentSurname,        String residentPosition,        String residentBirthday,        int individuadIdentificationCode,        String residentName,        String residentEmail,        int registrationCertificateCode,        String residentDepartment,        String residentPatronymic,        int id,        String residentUserType    ) {
        this.universityStructureUnit = universityStructureUnit;
        this.residentPassword = residentPassword;
        this.residentSurname = residentSurname;
        this.residentPosition = residentPosition;
        this.residentBirthday = residentBirthday;
        this.individuadIdentificationCode = individuadIdentificationCode;
        this.residentName = residentName;
        this.residentEmail = residentEmail;
        this.registrationCertificateCode = registrationCertificateCode;
        this.residentDepartment = residentDepartment;
        this.residentPatronymic = residentPatronymic;
        this.id = id;
        this.residentUserType = residentUserType;
    }


    public String getUniversitystructureunit() {
        return universityStructureUnit;
    }

    public void setUniversitystructureunit(String universityStructureUnit) {
        this.universityStructureUnit = universityStructureUnit;
    }
    public String getResidentpassword() {
        return residentPassword;
    }

    public void setResidentpassword(String residentPassword) {
        this.residentPassword = residentPassword;
    }
    public String getResidentsurname() {
        return residentSurname;
    }

    public void setResidentsurname(String residentSurname) {
        this.residentSurname = residentSurname;
    }
    public String getResidentposition() {
        return residentPosition;
    }

    public void setResidentposition(String residentPosition) {
        this.residentPosition = residentPosition;
    }
    public String getResidentbirthday() {
        return residentBirthday;
    }

    public void setResidentbirthday(String residentBirthday) {
        this.residentBirthday = residentBirthday;
    }
    public int getIndividuadidentificationcode() {
        return individuadIdentificationCode;
    }

    public void setIndividuadidentificationcode(int individuadIdentificationCode) {
        this.individuadIdentificationCode = individuadIdentificationCode;
    }
    public String getResidentname() {
        return residentName;
    }

    public void setResidentname(String residentName) {
        this.residentName = residentName;
    }
    public String getResidentemail() {
        return residentEmail;
    }

    public void setResidentemail(String residentEmail) {
        this.residentEmail = residentEmail;
    }
    public int getRegistrationcertificatecode() {
        return registrationCertificateCode;
    }

    public void setRegistrationcertificatecode(int registrationCertificateCode) {
        this.registrationCertificateCode = registrationCertificateCode;
    }
    public String getResidentdepartment() {
        return residentDepartment;
    }

    public void setResidentdepartment(String residentDepartment) {
        this.residentDepartment = residentDepartment;
    }
    public String getResidentpatronymic() {
        return residentPatronymic;
    }

    public void setResidentpatronymic(String residentPatronymic) {
        this.residentPatronymic = residentPatronymic;
    }
    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getResidentusertype() {
        return residentUserType;
    }

    public void setResidentusertype(String residentUserType) {
        this.residentUserType = residentUserType;
    }


}