





import java.util.List;
import java.util.ArrayList;

public class attroverridesecondarytable_Address  {

    private String city;
    private String street;
    private String name;





    private attroverridesecondarytable_NonEmployee attroverridesecondarytable_nonemployee;


    public attroverridesecondarytable_Address(
        String city,        String street,        String name    ) {
        this.city = city;
        this.street = street;
        this.name = name;
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
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public attroverridesecondarytable_NonEmployee getAttroverridesecondarytable_nonemployee() {
        return attroverridesecondarytable_nonemployee;
    }

    public void setAttroverridesecondarytable_nonemployee(attroverridesecondarytable_NonEmployee attroverridesecondarytable_nonemployee) {
        this.attroverridesecondarytable_nonemployee = attroverridesecondarytable_nonemployee;
    }

}