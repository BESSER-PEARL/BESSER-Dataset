





import java.util.List;
import java.util.ArrayList;

public class library_OclLibrary  {

    private String name;





    private List<library_OclExpression> library_oclexpressions;


    public library_OclLibrary(
        String name    ) {
        this.name = name;
        this.library_oclexpressions = new ArrayList<>();
    }

    public library_OclLibrary(
        String name        ArrayList<library_OclExpression> library_oclexpressions    ) {
        this.name = name;
        this.library_oclexpressions = library_oclexpressions;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public List<library_OclExpression> getLibrary_oclexpressions() {
        return library_oclexpressions;
    }

    public void addLibrary_oclexpression(Library_oclexpression library_oclexpression) {
        this.library_oclexpressions.add(library_oclexpression);
    }

}