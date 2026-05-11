





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPEnumerator extends OOPLEnumerator, CPPQualifiedNamedElement {

    private String cppValue;



    public cppmodel_CPPEnumerator(
        String cppValue    ) {
        super(
        );
        this.cppValue = cppValue;
    }


    public String getCppvalue() {
        return cppValue;
    }

    public void setCppvalue(String cppValue) {
        this.cppValue = cppValue;
    }


}