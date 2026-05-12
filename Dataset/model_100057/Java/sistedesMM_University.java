





import java.util.List;
import java.util.ArrayList;

public class sistedesMM_University  {

    private String name;
    private String country;
    private String provinceOrState;
    private String city;





    private sistedesMM_Person sistedesmm_person;


    public sistedesMM_University(
        String name,        String country,        String provinceOrState,        String city    ) {
        this.name = name;
        this.country = country;
        this.provinceOrState = provinceOrState;
        this.city = city;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getCountry() {
        return country;
    }

    public void setCountry(String country) {
        this.country = country;
    }
    public String getProvinceorstate() {
        return provinceOrState;
    }

    public void setProvinceorstate(String provinceOrState) {
        this.provinceOrState = provinceOrState;
    }
    public String getCity() {
        return city;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public sistedesMM_Person getSistedesmm_person() {
        return sistedesmm_person;
    }

    public void setSistedesmm_person(sistedesMM_Person sistedesmm_person) {
        this.sistedesmm_person = sistedesmm_person;
    }

}