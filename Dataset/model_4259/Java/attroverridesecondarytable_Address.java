





import java.util.List;
import java.util.ArrayList;

public class attroverridesecondarytable_Address  {

    private String street;
    private String name;
    private String city;





    private attroverridesecondarytable_NonEmployee attroverridesecondarytable_nonemployee;




    private attroverridesecondarytable_Employee attroverridesecondarytable_employee;


    public attroverridesecondarytable_Address(
        String street,        String name,        String city    ) {
        this.street = street;
        this.name = name;
        this.city = city;
    }


    public String getStreet() {
        return street;
    }

    public void setStreet(String street) {
        this.street = street;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public attroverridesecondarytable_NonEmployee getAttroverridesecondarytable_nonemployee() {
        return attroverridesecondarytable_nonemployee;
    }

    public void setAttroverridesecondarytable_nonemployee(attroverridesecondarytable_NonEmployee attroverridesecondarytable_nonemployee) {
        this.attroverridesecondarytable_nonemployee = attroverridesecondarytable_nonemployee;
    }
    public attroverridesecondarytable_Employee getAttroverridesecondarytable_employee() {
        return attroverridesecondarytable_employee;
    }

    public void setAttroverridesecondarytable_employee(attroverridesecondarytable_Employee attroverridesecondarytable_employee) {
        this.attroverridesecondarytable_employee = attroverridesecondarytable_employee;
    }

}