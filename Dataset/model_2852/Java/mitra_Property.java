





import java.util.List;
import java.util.ArrayList;

public class mitra_Property  {

    private String name;
    private String value;





    private mitra_MetamodelDeclaration mitra_metamodeldeclaration;




    private mitra_JavaSpec mitra_javaspec;


    public mitra_Property(
        String name,        String value    ) {
        this.name = name;
        this.value = value;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }

    public mitra_MetamodelDeclaration getMitra_metamodeldeclaration() {
        return mitra_metamodeldeclaration;
    }

    public void setMitra_metamodeldeclaration(mitra_MetamodelDeclaration mitra_metamodeldeclaration) {
        this.mitra_metamodeldeclaration = mitra_metamodeldeclaration;
    }
    public mitra_JavaSpec getMitra_javaspec() {
        return mitra_javaspec;
    }

    public void setMitra_javaspec(mitra_JavaSpec mitra_javaspec) {
        this.mitra_javaspec = mitra_javaspec;
    }

}