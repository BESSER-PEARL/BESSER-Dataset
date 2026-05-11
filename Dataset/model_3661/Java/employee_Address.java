





import java.util.List;
import java.util.ArrayList;

public class employee_Address  {

    private String city;
    private String street;
    private String postalCode;
    private String country;
    private String province;





    private employee_Employee employee_employee;


    public employee_Address(
        String city,        String street,        String postalCode,        String country,        String province    ) {
        this.city = city;
        this.street = street;
        this.postalCode = postalCode;
        this.country = country;
        this.province = province;
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
    public String getPostalcode() {
        return postalCode;
    }

    public void setPostalcode(String postalCode) {
        this.postalCode = postalCode;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
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