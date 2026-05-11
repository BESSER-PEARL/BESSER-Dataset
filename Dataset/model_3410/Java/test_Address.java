





import java.util.List;
import java.util.ArrayList;

public class test_Address  {

    private String city;
    private String street;





    private test_Person test_person;


    public test_Address(
        String city,        String street    ) {
        this.city = city;
        this.street = street;
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

    public test_Person getTest_person() {
        return test_person;
    }

    public void setTest_person(test_Person test_person) {
        this.test_person = test_person;
    }

}