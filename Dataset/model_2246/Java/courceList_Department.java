





import java.util.List;
import java.util.ArrayList;

public class courceList_Department  {

    private String name;
    private String abbreviation;



    public courceList_Department(
        String name,        String abbreviation    ) {
        this.name = name;
        this.abbreviation = abbreviation;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getAbbreviation() {
        return abbreviation;
    }

    public void setAbbreviation(String abbreviation) {
        this.abbreviation = abbreviation;
    }


}