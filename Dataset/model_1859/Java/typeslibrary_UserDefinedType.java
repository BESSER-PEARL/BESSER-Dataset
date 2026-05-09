





import java.util.List;
import java.util.ArrayList;

public class typeslibrary_UserDefinedType  {

    private String name;





    private typeslibrary_ComplexNamedType typeslibrary_complexnamedtype;




    private typeslibrary_UserDefinedTypesLibrary typeslibrary_userdefinedtypeslibrary;


    public typeslibrary_UserDefinedType(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public typeslibrary_ComplexNamedType getTypeslibrary_complexnamedtype() {
        return typeslibrary_complexnamedtype;
    }

    public void setTypeslibrary_complexnamedtype(typeslibrary_ComplexNamedType typeslibrary_complexnamedtype) {
        this.typeslibrary_complexnamedtype = typeslibrary_complexnamedtype;
    }
    public typeslibrary_UserDefinedTypesLibrary getTypeslibrary_userdefinedtypeslibrary() {
        return typeslibrary_userdefinedtypeslibrary;
    }

    public void setTypeslibrary_userdefinedtypeslibrary(typeslibrary_UserDefinedTypesLibrary typeslibrary_userdefinedtypeslibrary) {
        this.typeslibrary_userdefinedtypeslibrary = typeslibrary_userdefinedtypeslibrary;
    }

}