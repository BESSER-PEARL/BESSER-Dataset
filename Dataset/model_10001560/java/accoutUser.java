





import java.util.List;
import java.util.ArrayList;

public class accoutUser  {

    private String passwordUser;
    private String emailUser;
    private String dateRegister;
    private int idUser;
    private String codeConfirm;
    private int idCompany;





    private List<Car> cars;




    private infoCompany infocompany;


    public accoutUser(
        String passwordUser,        String emailUser,        String dateRegister,        int idUser,        String codeConfirm,        int idCompany    ) {
        this.passwordUser = passwordUser;
        this.emailUser = emailUser;
        this.dateRegister = dateRegister;
        this.idUser = idUser;
        this.codeConfirm = codeConfirm;
        this.idCompany = idCompany;
        this.cars = new ArrayList<>();
    }

    public accoutUser(
        String passwordUser,        String emailUser,        String dateRegister,        int idUser,        String codeConfirm,        int idCompany        ArrayList<Car> cars    ) {
        this.passwordUser = passwordUser;
        this.emailUser = emailUser;
        this.dateRegister = dateRegister;
        this.idUser = idUser;
        this.codeConfirm = codeConfirm;
        this.idCompany = idCompany;
        this.cars = cars;
    }

    public String getPassworduser() {
        return passwordUser;
    }

    public void setPassworduser(String passwordUser) {
        this.passwordUser = passwordUser;
    }
    public String getEmailuser() {
        return emailUser;
    }

    public void setEmailuser(String emailUser) {
        this.emailUser = emailUser;
    }
    public String getDateregister() {
        return dateRegister;
    }

    public void setDateregister(String dateRegister) {
        this.dateRegister = dateRegister;
    }
    public int getIduser() {
        return idUser;
    }

    public void setIduser(int idUser) {
        this.idUser = idUser;
    }
    public String getCodeconfirm() {
        return codeConfirm;
    }

    public void setCodeconfirm(String codeConfirm) {
        this.codeConfirm = codeConfirm;
    }
    public int getIdcompany() {
        return idCompany;
    }

    public void setIdcompany(int idCompany) {
        this.idCompany = idCompany;
    }

    public List<Car> getCars() {
        return cars;
    }

    public void addCar(Car car) {
        this.cars.add(car);
    }
    public infoCompany getInfocompany() {
        return infocompany;
    }

    public void setInfocompany(infoCompany infocompany) {
        this.infocompany = infocompany;
    }

}