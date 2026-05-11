





import java.util.List;
import java.util.ArrayList;

public class r1_CodeSystemRef extends Expression {

    private String name;
    private String libraryName;





    private r1_InCodeSystem r1_incodesystem;




    private r1_Code r1_code;


    public r1_CodeSystemRef(
        String name,        String libraryName    ) {
        super(
        );
        this.name = name;
        this.libraryName = libraryName;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getLibraryname() {
        return libraryName;
    }

    public void setLibraryname(String libraryName) {
        this.libraryName = libraryName;
    }

    public r1_InCodeSystem getR1_incodesystem() {
        return r1_incodesystem;
    }

    public void setR1_incodesystem(r1_InCodeSystem r1_incodesystem) {
        this.r1_incodesystem = r1_incodesystem;
    }
    public r1_Code getR1_code() {
        return r1_code;
    }

    public void setR1_code(r1_Code r1_code) {
        this.r1_code = r1_code;
    }

}