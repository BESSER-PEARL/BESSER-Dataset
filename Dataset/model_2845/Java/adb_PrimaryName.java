





import java.util.List;
import java.util.ArrayList;

public class adb_PrimaryName  {






    private adb_Name adb_name;




    private List<adb_ParameterAssociation> adb_parameterassociations;




    private adb_PrimaryName adb_primaryname;




    private adb_Name adb_name;


    public adb_PrimaryName(
    ) {
        this.adb_parameterassociations = new ArrayList<>();
    }

    public adb_PrimaryName(
        ArrayList<adb_ParameterAssociation> adb_parameterassociations    ) {
        this.adb_parameterassociations = adb_parameterassociations;
    }


    public adb_Name getAdb_name() {
        return adb_name;
    }

    public void setAdb_name(adb_Name adb_name) {
        this.adb_name = adb_name;
    }
    public List<adb_ParameterAssociation> getAdb_parameterassociations() {
        return adb_parameterassociations;
    }

    public void addAdb_parameterassociation(Adb_parameterassociation adb_parameterassociation) {
        this.adb_parameterassociations.add(adb_parameterassociation);
    }
    public adb_PrimaryName getAdb_primaryname() {
        return adb_primaryname;
    }

    public void setAdb_primaryname(adb_PrimaryName adb_primaryname) {
        this.adb_primaryname = adb_primaryname;
    }
    public adb_Name getAdb_name() {
        return adb_name;
    }

    public void setAdb_name(adb_Name adb_name) {
        this.adb_name = adb_name;
    }

}