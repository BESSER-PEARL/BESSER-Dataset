





import java.util.List;
import java.util.ArrayList;

public class gedcoml_Address  {

    private String exodus;
    private String entry;





    private gedcoml_Person gedcoml_person;


    public gedcoml_Address(
        String exodus,        String entry    ) {
        this.exodus = exodus;
        this.entry = entry;
    }


    public String getExodus() {
        return exodus;
    }

    public void setExodus(String exodus) {
        this.exodus = exodus;
    }
    public String getEntry() {
        return entry;
    }

    public void setEntry(String entry) {
        this.entry = entry;
    }

    public gedcoml_Person getGedcoml_person() {
        return gedcoml_person;
    }

    public void setGedcoml_person(gedcoml_Person gedcoml_person) {
        this.gedcoml_person = gedcoml_person;
    }

}