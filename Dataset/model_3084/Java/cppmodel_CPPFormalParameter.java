





import java.util.List;
import java.util.ArrayList;

public class cppmodel_CPPFormalParameter extends CPPQualifiedNamedElement {

    private String passingMode;



    public cppmodel_CPPFormalParameter(
        String passingMode    ) {
        super(
        );
        this.passingMode = passingMode;
    }


    public String getPassingmode() {
        return passingMode;
    }

    public void setPassingmode(String passingMode) {
        this.passingMode = passingMode;
    }


}