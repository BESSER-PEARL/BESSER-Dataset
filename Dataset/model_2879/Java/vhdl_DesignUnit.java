





import java.util.List;
import java.util.ArrayList;

public class vhdl_DesignUnit extends VhdlObject {

    private String library;



    public vhdl_DesignUnit(
        String library    ) {
        super(
        );
        this.library = library;
    }


    public String getLibrary() {
        return library;
    }

    public void setLibrary(String library) {
        this.library = library;
    }


}