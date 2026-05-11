




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class sample_Person  {

    private LocalDate birthdate;
    private String name;





    private sample_Group sample_group;




    private sample_Group sample_group;


    public sample_Person(
        LocalDate birthdate,        String name    ) {
        this.birthdate = birthdate;
        this.name = name;
    }


    public LocalDate getBirthdate() {
        return birthdate;
    }

    public void setBirthdate(LocalDate birthdate) {
        this.birthdate = birthdate;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public sample_Group getSample_group() {
        return sample_group;
    }

    public void setSample_group(sample_Group sample_group) {
        this.sample_group = sample_group;
    }
    public sample_Group getSample_group() {
        return sample_group;
    }

    public void setSample_group(sample_Group sample_group) {
        this.sample_group = sample_group;
    }

}