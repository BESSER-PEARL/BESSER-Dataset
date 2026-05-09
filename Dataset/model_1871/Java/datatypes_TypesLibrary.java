





import java.util.List;
import java.util.ArrayList;

public class datatypes_TypesLibrary  {

    private String name;





    private List<datatypes_TypesLibrary> datatypes_typeslibrarys;


    public datatypes_TypesLibrary(
        String name    ) {
        this.name = name;
        this.datatypes_typeslibrarys = new ArrayList<>();
    }

    public datatypes_TypesLibrary(
        String name        ArrayList<datatypes_TypesLibrary> datatypes_typeslibrarys    ) {
        this.name = name;
        this.datatypes_typeslibrarys = datatypes_typeslibrarys;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<datatypes_TypesLibrary> getDatatypes_typeslibrarys() {
        return datatypes_typeslibrarys;
    }

    public void addDatatypes_typeslibrary(Datatypes_typeslibrary datatypes_typeslibrary) {
        this.datatypes_typeslibrarys.add(datatypes_typeslibrary);
    }

}