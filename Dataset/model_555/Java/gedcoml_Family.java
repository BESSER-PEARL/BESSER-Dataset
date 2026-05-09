





import java.util.List;
import java.util.ArrayList;

public class gedcoml_Family  {

    private String name;





    private List<gedcoml_FamilyImport> gedcoml_familyimports;




    private gedcoml_FamilyImport gedcoml_familyimport;


    public gedcoml_Family(
        String name    ) {
        this.name = name;
        this.gedcoml_familyimports = new ArrayList<>();
    }

    public gedcoml_Family(
        String name        ArrayList<gedcoml_FamilyImport> gedcoml_familyimports    ) {
        this.name = name;
        this.gedcoml_familyimports = gedcoml_familyimports;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<gedcoml_FamilyImport> getGedcoml_familyimports() {
        return gedcoml_familyimports;
    }

    public void addGedcoml_familyimport(Gedcoml_familyimport gedcoml_familyimport) {
        this.gedcoml_familyimports.add(gedcoml_familyimport);
    }
    public gedcoml_FamilyImport getGedcoml_familyimport() {
        return gedcoml_familyimport;
    }

    public void setGedcoml_familyimport(gedcoml_FamilyImport gedcoml_familyimport) {
        this.gedcoml_familyimport = gedcoml_familyimport;
    }

}