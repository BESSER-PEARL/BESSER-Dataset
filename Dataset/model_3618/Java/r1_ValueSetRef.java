





import java.util.List;
import java.util.ArrayList;

public class r1_ValueSetRef extends Expression {

    private String name;
    private String libraryName;





    private r1_InValueSet r1_invalueset;


    public r1_ValueSetRef(
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

    public r1_InValueSet getR1_invalueset() {
        return r1_invalueset;
    }

    public void setR1_invalueset(r1_InValueSet r1_invalueset) {
        this.r1_invalueset = r1_invalueset;
    }

}