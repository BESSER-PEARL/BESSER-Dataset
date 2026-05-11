





import java.util.List;
import java.util.ArrayList;

public class employee_Address  {

    private int id;
    private String city;
    private String street;
    private String country;
    private String postalCode;
    private String province;





    private employee_Employee employee_employee;


    public employee_Address(
        int id,        String city,        String street,        String country,        String postalCode,        String province    ) {
        this.id = id;
        this.city = city;
        this.street = street;
        this.country = country;
        this.postalCode = postalCode;
        this.province = province;
    }


    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }
    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }

    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }

}