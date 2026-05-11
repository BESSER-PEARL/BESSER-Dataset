





import java.util.List;
import java.util.ArrayList;

public class employee_Address  {

    private String country;
    private String street;
    private String province;
    private String city;
    private String postalCode;
    private String id;





    private employee_Employee employee_employee;


    public employee_Address(
        String country,        String street,        String province,        String city,        String postalCode,        String id    ) {
        this.country = country;
        this.street = street;
        this.province = province;
        this.city = city;
        this.postalCode = postalCode;
        this.id = id;
    }


    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getProvince() {
        return province;
    }

    public void setProvince(String province) {
        this.province = province;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }
    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public employee_Employee getEmployee_employee() {
        return employee_employee;
    }

    public void setEmployee_employee(employee_Employee employee_employee) {
        this.employee_employee = employee_employee;
    }

}