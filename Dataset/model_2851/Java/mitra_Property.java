





import java.util.List;
import java.util.ArrayList;

public class mitra_Property  {

    private String value;
    private String name;





    private mitra_MetamodelDeclaration mitra_metamodeldeclaration;


    public mitra_Property(
        String value,        String name    ) {
        this.value = value;
        this.name = name;
    }


    public String getValue() {
        return value;
    }

    public void setValue(String value) {
        this.value = value;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mitra_MetamodelDeclaration getMitra_metamodeldeclaration() {
        return mitra_metamodeldeclaration;
    }

    public void setMitra_metamodeldeclaration(mitra_MetamodelDeclaration mitra_metamodeldeclaration) {
        this.mitra_metamodeldeclaration = mitra_metamodeldeclaration;
    }

}