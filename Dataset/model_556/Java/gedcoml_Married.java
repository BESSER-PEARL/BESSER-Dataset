





import java.util.List;
import java.util.ArrayList;

public class gedcoml_Married  {

    private String weddingDay;
    private String separationDay;





    private gedcoml_BekanntePerson gedcoml_bekannteperson;




    private gedcoml_Person gedcoml_person;


    public gedcoml_Married(
        String weddingDay,        String separationDay    ) {
        this.weddingDay = weddingDay;
        this.separationDay = separationDay;
    }


    public String getWeddingday() {
        return weddingDay;
    }

    public void setWeddingday(String weddingDay) {
        this.weddingDay = weddingDay;
    }
    public String getSeparationday() {
        return separationDay;
    }

    public void setSeparationday(String separationDay) {
        this.separationDay = separationDay;
    }

    public gedcoml_BekanntePerson getGedcoml_bekannteperson() {
        return gedcoml_bekannteperson;
    }

    public void setGedcoml_bekannteperson(gedcoml_BekanntePerson gedcoml_bekannteperson) {
        this.gedcoml_bekannteperson = gedcoml_bekannteperson;
    }
    public gedcoml_Person getGedcoml_person() {
        return gedcoml_person;
    }

    public void setGedcoml_person(gedcoml_Person gedcoml_person) {
        this.gedcoml_person = gedcoml_person;
    }

}