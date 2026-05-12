





import java.util.List;
import java.util.ArrayList;

public class Person  {

    private String id;
    private String phNum;
    private String PersonFName;



    public Person(
        String id,        String phNum,        String PersonFName    ) {
        this.id = id;
        this.phNum = phNum;
        this.PersonFName = PersonFName;
    }


    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }
    public String getPhnum() {
        return phNum;
    }

    public void setPhnum(String phNum) {
        this.phNum = phNum;
    }
    public String getPersonfname() {
        return PersonFName;
    }

    public void setPersonfname(String PersonFName) {
        this.PersonFName = PersonFName;
    }


}