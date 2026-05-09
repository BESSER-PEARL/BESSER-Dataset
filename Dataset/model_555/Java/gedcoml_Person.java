





import java.util.List;
import java.util.ArrayList;

public class gedcoml_Person  {

    private String id;
    private String sex;





    private gedcoml_Married gedcoml_married;




    private gedcoml_Family gedcoml_family;


    public gedcoml_Person(
        String id,        String sex    ) {
        this.id = id;
        this.sex = sex;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getSex() {
        return sex;
    }

    public void setSex(String sex) {
        this.sex = sex;
    }

    public gedcoml_Married getGedcoml_married() {
        return gedcoml_married;
    }

    public void setGedcoml_married(gedcoml_Married gedcoml_married) {
        this.gedcoml_married = gedcoml_married;
    }
    public gedcoml_Family getGedcoml_family() {
        return gedcoml_family;
    }

    public void setGedcoml_family(gedcoml_Family gedcoml_family) {
        this.gedcoml_family = gedcoml_family;
    }

}