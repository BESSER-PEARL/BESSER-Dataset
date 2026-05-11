





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPBasicType extends OOPLBasicType, CPPQualifiedNamedElement {

    private String cppSpecifier;



    public cppmodel_CPPBasicType(
        String cppSpecifier    ) {
        super(
        );
        this.cppSpecifier = cppSpecifier;
    }


    public String getCppspecifier() {
        return cppSpecifier;
    }

    public void setCppspecifier(String cppSpecifier) {
        this.cppSpecifier = cppSpecifier;
    }


}